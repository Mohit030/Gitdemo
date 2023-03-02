#pytest method names should start with test
import pytest


#Any pytest file always starts with test_
# any code should be wrapped in method only
#method name should name have sense
@pytest.mark.smoke# used to mark and run particular testcases
@pytest.mark.skip# used to skip particular test case
def test_firstprogram():
    msg='hello'
    assert msg =="Hi","Test failed"

@pytest.mark.xskip# it will use when this will run but pass or fail we cant see on output , wecant see that on report
def test_secondcreditcard():
    a=4
    b=6
    assert a+2==6,"Addition do not match"

