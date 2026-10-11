#!/usr/bin/env python3
"""send_report_email.py — Send the nightly HTML report as an email.

Usage:
    python send_report_email.py \
        --html-file  <path to report.html> \
        --subject    "TileOPs Nightly Report 20260318_220000" \
        --to         gaoang0125@163.com

Environment variables (required):
    MAIL_SMTP_SERVER   — SMTP server (e.g. smtp.163.com)
    MAIL_SMTP_PORT     — SMTP port (e.g. 465 for SSL, 587 for STARTTLS)
    MAIL_USERNAME      — sender email address
    MAIL_PASSWORD      — SMTP authorization code (NOT login password for 163.com)
"""

import argparse
import os
import smtplib
import ssl
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path


def send_email(
    smtp_server: str,
    smtp_port: int,
    username: str,
    password: str,
    to_addr: str,
    subject: str,
    html_body: str,
) -> None:
    msg = MIMEMultipart("alternative")
    msg["From"] = username
    msg["To"] = to_addr
    msg["Subject"] = subject

    # Plain-text fallback
    msg.attach(MIMEText("请使用支持 HTML 的邮件客户端查看此报告。", "plain", "utf-8"))
    # HTML body
    msg.attach(MIMEText(html_body, "html", "utf-8"))

    context = ssl.create_default_context()

    if smtp_port == 465:
        # SSL
        with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
            server.login(username, password)
            server.sendmail(username, to_addr, msg.as_string())
    else:
        # STARTTLS (port 587, 25, etc.)
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls(context=context)
            server.login(username, password)
            server.sendmail(username, to_addr, msg.as_string())


def main() -> None:
    parser = argparse.ArgumentParser(description="Send nightly HTML report via email")
    parser.add_argument("--html-file", required=True, help="Path to report.html")
    parser.add_argument("--subject", required=True, help="Email subject line")
    parser.add_argument("--to", required=True, help="Recipient email address")
    args = parser.parse_args()

    smtp_server = os.environ.get("MAIL_SMTP_SERVER", "")
    smtp_port   = int(os.environ.get("MAIL_SMTP_PORT", "465"))
    username    = os.environ.get("MAIL_USERNAME", "")
    password    = os.environ.get("MAIL_PASSWORD", "")

    if not all([smtp_server, username, password]):
        print(
            "::warning::MAIL_SMTP_SERVER / MAIL_USERNAME / MAIL_PASSWORD not set — "
            "skipping email.",
            file=sys.stderr,
        )
        sys.exit(0)

    html_path = Path(args.html_file)
    if not html_path.exists():
        print(f"::warning::HTML file not found: {args.html_file} — skipping email.",
              file=sys.stderr)
        sys.exit(0)

    html_body = html_path.read_text(encoding="utf-8")
    print(f"Sending report email to {args.to} ...")
    try:
        send_email(smtp_server, smtp_port, username, password,
                   args.to, args.subject, html_body)
        print(f"Email sent successfully to {args.to}")
    except Exception as exc:
        print(f"::warning::Failed to send email: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
