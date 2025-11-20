from hello import more_hello, more_goodbye


def test_more_hello():
    assert "hi" == more_hello()


def test_more_oodbye():
    assert "bye" == more_goodbye()
