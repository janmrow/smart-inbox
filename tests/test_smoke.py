from smart_inbox.__main__ import main


def test_main(capsys) -> None:
    main()
    assert capsys.readouterr().out == "Smart Inbox\n"
