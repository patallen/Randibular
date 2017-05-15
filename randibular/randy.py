import random
from string import ascii_lowercase as asciis


NAMES = ["Jose", "Vendela", "Joe", "Waldron", "Hampus", "Jonathan", "Viktor"]


def random_name():
    """Grab a random name from the NAMES above."""
    return NAMES[random.randint(0, len(NAMES) - 1)]


def name_value(name):
    """Add the value of the letters of a name.

    >>> name_value("bob")
    16

    >>> name_value("aba")
    1
    """
    mapped = dict([(a, i) for (i, a) in enumerate(asciis)])
    name = name.replace(" ", "")
    try:
        rv = sum([mapped[l.lower()] for l in name])
    except KeyError as e:
        raise Exception("Wut?: {} isn't ascii, sorry.".format(e))

    return rv


def name_value_averaged(name):
    """A more fair assessment of a person's worth.

    >>> name_value_averaged("Joe")
    9.0
    """
    value = name_value(name)
    return value / float(len(name))


def inform_random():
    """Pick a user at random, return message containing his/her name value."""
    name = random_name()
    value = name_value(name)

    thought = "Hey {name}! I heard your name is worth {value}!?!?"
    return thought.format(name=name, value=value)

def inform_user_email():
    """Pick a random user and email her value."""
    rand_user = random_name()
    value = name_value(rand_user)
    email = "{}@bison.co".format(rand_user)
    send_email(email="{}".format(email), value=value)


def send_email(email, message):
    """Function that sends a message to a user via email."""
    raise Exception("This email would totally go to {}".format(email))
