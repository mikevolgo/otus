from main import foo


def test_main():
    assert True


def test_foo():
    assert foo(1) == 1, f"Failed test foo."
