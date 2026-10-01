import imaplib
import os
import smtplib
import ssl
from email import policy
from email.message import EmailMessage
from email.parser import BytesParser
from email.utils import formatdate, make_msgid


def build_reply(
    raw_message: bytes, from_address: str, allowed_sender: str
) -> EmailMessage | None:
    incoming = BytesParser(policy=policy.default).parsebytes(raw_message)
    from_headers = incoming.get_all("From", [])
    if len(from_headers) != 1 or len(from_headers[0].addresses) != 1:
        return None
    sender = from_headers[0].addresses[0].addr_spec
    if sender.casefold() != allowed_sender.casefold():
        return None

    body_part = incoming.get_body(preferencelist=("plain",))
    if body_part is None:
        raise ValueError("Incoming message has no plain-text body")

    subject = str(incoming.get("Subject", ""))
    reply = EmailMessage()
    reply["From"] = from_address
    reply["To"] = sender
    reply["Subject"] = f"Re: {subject}" if subject else "Re: (no subject)"
    reply["Date"] = formatdate(localtime=True)
    reply["Message-ID"] = make_msgid()
    if message_id := incoming.get("Message-ID"):
        reply["In-Reply-To"] = str(message_id)
        reply["References"] = f"{incoming.get('References', '')} {message_id}".strip()
    reply.set_content(f"You wrote: {body_part.get_content().strip()}")
    return reply


def main() -> None:
    required = (
        "SMART_INBOX_EMAIL",
        "SMART_INBOX_APP_PASSWORD",
        "SMART_INBOX_ALLOWED_SENDER",
    )
    missing = [name for name in required if not os.getenv(name)]
    if missing:
        raise SystemExit(f"Missing environment variables: {', '.join(missing)}")

    email_address = os.environ["SMART_INBOX_EMAIL"]
    password = os.environ["SMART_INBOX_APP_PASSWORD"]
    allowed_sender = os.environ["SMART_INBOX_ALLOWED_SENDER"].strip()
    if not allowed_sender:
        raise SystemExit("SMART_INBOX_ALLOWED_SENDER must be an email address")
    tls = ssl.create_default_context()

    with imaplib.IMAP4_SSL("imap.gmail.com", port=993, ssl_context=tls) as inbox:
        inbox.login(email_address, password)
        status, _ = inbox.select("INBOX")
        if status != "OK":
            raise RuntimeError("Cannot select INBOX")

        status, data = inbox.uid(
            "search", None, "UNSEEN", "FROM", f'"{allowed_sender}"'
        )
        if status != "OK":
            raise RuntimeError("Cannot search INBOX")
        uids = data[0].split()
        for uid in uids:
            status, data = inbox.uid("fetch", uid, "(BODY.PEEK[])")
            if status != "OK":
                raise RuntimeError("Cannot fetch message")
            raw_message = next(part[1] for part in data if isinstance(part, tuple))
            reply = build_reply(raw_message, email_address, allowed_sender)
            if reply is None:
                continue

            with smtplib.SMTP("smtp.gmail.com", port=587) as smtp:
                smtp.starttls(context=tls)
                smtp.login(email_address, password)
                smtp.send_message(reply)

            status, _ = inbox.uid("store", uid, "+FLAGS", "(\\Seen)")
            if status != "OK":
                raise RuntimeError("Reply sent, but could not mark message as read")

            print("Echo reply sent")
            return

    print("No unread messages from allowed sender")


if __name__ == "__main__":
    main()
