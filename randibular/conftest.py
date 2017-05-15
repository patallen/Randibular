"""
conftest.py seems to be where shared stuff goes.

We an have fixtures that can be applied to tests individually, by the
module, or for the entirity of the session (global)
"""


import pytest


@pytest.fixture
def no_email(mocker):
    """
    A globally available fixture that can be passed to test
    functions to send randy.send_email calls to a MagicMock.
    """
    fake_email = mocker.MagicMock()
    mocker.patch('randibular.randy.send_email', fake_email)
    return fake_email
