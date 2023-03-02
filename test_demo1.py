#pytest method names should start with test
import pytest


#Any pytest file always starts with test_
# any code should be wrapped in method only
@pytest.mark.smoke
def test_firstprogram():
    print("hello")


def test_secondprogram():
        print("good morning")
