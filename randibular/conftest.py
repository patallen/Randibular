import pytest


@pytest.fixture
def no_email(mocker):
    fake_email = mocker.MagicMock()
    mocker.patch('randibular.randy.send_email', fake_email)
    return fake_email
