import pytest
import mock

from randibular import randy


@pytest.mark.one
def test_name_value():
    """Test the fuctionality of randy.name_value."""
    patrick = "patrick"

    assert randy.name_value(patrick) == 71
    assert randy.name_value("Patrick") == randy.name_value("patrick")


@pytest.mark.two
def test_name_value_invalid_char():
    """Test that characters not in NAMES constant raise an error."""
    j_money = "jo$e"

    with pytest.raises(Exception) as e:
        randy.name_value(j_money)


@pytest.mark.three
@pytest.mark.parametrize("name, expected", [
    ("bob", 16), ("Xavier Zachary", 148), ("Abe", 5), ("Stove Jobes", 122)
])
def test_name_value_multi(name, expected):
    """Test mulitple inputs/outputs using pytest's parametrize"""
    assert randy.name_value(name) == expected


@pytest.mark.four
def test_random_value_inform(mocker):
    """
    Monkeypatch the standard library function 'random.randint' to always return
    the value 4 in this test.

    EX: We can monkeypatch 'datamonster.waitfor' to return an instant known result
    """
    mocker.patch('random.randint', return_value=4)
    exclamation = randy.inform_random()
    assert exclamation == "Hey Hampus! I heard your name is worth 72!?!?"


@pytest.mark.five
def test_inform_user_email(mocker):
    """Use MagicMock to determine of a function was called as expected."""
    mocker.patch('random.randint', return_value=4)

    # We mock the send_email function with an imaginary function
    mock_send_email = mock.MagicMock()
    mocker.patch('randibular.randy.send_email', new=mock_send_email)

    # Assert the inner funcion was called with the expected params
    randy.inform_user_email()
    mock_send_email.assert_called_with(email="Hampus@bison.co", value=72)


@pytest.mark.six
def test_global_fixtures(no_email):
    """
    We can do the same types of things, but even easier by creating a shared fixture.

    """
    randy.send_email("president@whitehouse.gov", 0)

    # send_email is never called, but we can still use the resulting MagicMock
    # we are using this to replace 'datamonster.wait_for' with a function that bypasses the dm caching
    no_email.assert_called()


@pytest.mark.seven
@pytest.mark.approx
def test_approximate_name_value():
    """Use pytest.approximate to test for approximate return values.

    This is good for us because:
        - Floating point numbers are deceiving
        - We may want to check that a result is within a target range.
    """
    waldron_worth = randy.name_value_averaged("Waldron")

    # assert waldron_worth == 11.4285714286
    assert pytest.approx(waldron_worth, .0001) == 11.4285714286

    # Assert something is within += specified range
    # meaning: (7.654321 +- 1%) == 7.654300
    assert pytest.approx(7.65431, 0.01) == 7.654300
