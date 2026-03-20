#!/usr/bin/env python3
"""send_report_email.py — Send the nightly HTML report as an email.

Usage:
    python send_report_email.py \
        --html-file  <path to report.html> \
        --subject    "TileOPs Nightly Report 20260318_220000" \
        --recipients-file scripts/email_recipients.txt

    Or with explicit addresses (overrides --recipients-file):
    python send_report_email.py \
        --html-file  <path to report.html> \
        --subject    "TileOPs Nightly Report 20260318_220000" \
        --to         addr1@example.com addr2@example.com

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


def load_recipients(filepath: str) -> list[str]:
    """Load email addresses from a file, one per line. Ignore comments and blanks."""
    path = Path(filepath)
    if not path.exists():
        print(f"::warning::Recipients file not found: {filepath}", file=sys.stderr)
        return []
    recipients = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            recipients.append(line)
    return recipients


def send_email(
    smtp_server: str,
    smtp_port: int,
    username: str,
    password: str,
    to_addrs: list[str],
    subject: str,
    html_body: str,
) -> None:
    msg = MIMEMultipart("alternative")
    msg["From"] = username
    msg["To"] = ", ".join(to_addrs)
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
            server.sendmail(username, to_addrs, msg.as_string())
    else:
        # STARTTLS (port 587, 25, etc.)
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls(context=context)
            server.login(username, password)
            server.sendmail(username, to_addrs, msg.as_string())


def main() -> None:
    parser = argparse.ArgumentParser(description="Send nightly HTML report via email")
    parser.add_argument("--html-file", required=True, help="Path to report.html")
    parser.add_argument("--subject", required=True, help="Email subject line")
    parser.add_argument("--to", nargs="+", default=[], help="Recipient email address(es)")
    parser.add_argument("--recipients-file", default=None,
                        help="Path to file with recipient emails (one per line)")
    args = parser.parse_args()

    # Resolve recipients: --to takes priority; fall back to --recipients-file
    recipients = args.to
    if not recipients and args.recipients_file:
        recipients = load_recipients(args.recipients_file)
    if not recipients:
        print("::warning::No recipients specified — skipping email.", file=sys.stderr)
        sys.exit(0)

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
    recipient_list = ", ".join(recipients)
    print(f"Sending report email to {recipient_list} ...")
    try:
        send_email(smtp_server, smtp_port, username, password,
                   recipients, args.subject, html_body)
        print(f"Email sent successfully to {recipient_list}")
    except Exception as exc:
        print(f"::warning::Failed to send email: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
