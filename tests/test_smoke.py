from email.message import EmailMessage

from smart_inbox.__main__ import build_reply


def test_reply_echoes_plain_text_from_multipart_email() -> None:
    incoming = EmailMessage()
    incoming["From"] = "Alice <alice@example.com>"
    incoming["Subject"] = "Żółw?"
    incoming["Message-ID"] = "<original@example.com>"
    incoming.set_content("Hello from my phone")
    incoming.add_alternative("<p>HTML version</p>", subtype="html")

    reply = build_reply(incoming.as_bytes(), "inbox@example.com", "alice@example.com")

    assert reply is not None
    assert reply["From"] == "inbox@example.com"
    assert reply["To"] == "alice@example.com"
    assert reply["Subject"] == "Re: Żółw?"
    assert reply["Date"]
    assert reply["Message-ID"]
    assert reply["In-Reply-To"] == "<original@example.com>"
    assert reply["References"] == "<original@example.com>"
    assert reply.get_content() == "You wrote: Hello from my phone\n"


def test_reply_ignores_mail_from_other_sender() -> None:
    incoming = EmailMessage()
    incoming["From"] = "Bob <bob@example.com>"
    incoming.set_content("Hello")

    assert (
        build_reply(incoming.as_bytes(), "inbox@example.com", "alice@example.com")
        is None
    )


def test_reply_requires_exactly_one_allowed_from_address() -> None:
    for from_header in (
        '"alice@example.com" <other@example.com>',
        "Alice <alice@example.com.evil>",
        "alice@example.com, other@example.com",
    ):
        incoming = EmailMessage()
        incoming["From"] = from_header
        incoming.set_content("Hello")

        assert (
            build_reply(incoming.as_bytes(), "inbox@example.com", "alice@example.com")
            is None
        )

    duplicate_from = b"From: alice@example.com\r\nFrom: other@example.com\r\n\r\nHello"
    assert build_reply(duplicate_from, "inbox@example.com", "alice@example.com") is None
