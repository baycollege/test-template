from pytest import raises

from .context import basic_functions, test_template


def test_add_positive():

    num1 = 1
    num2 = 2

    result = basic_functions.add(num1, num2)

    assert result == 3


def test_add_negative():

    num1 = -1
    num2 = -2

    result = basic_functions.add(num1, num2)

    assert result == -3


def test_sub():

    num1 = 2
    num2 = 1

    result = basic_functions.sub(num1, num2)

    assert result == 1


def test_sub_negative():

    num1 = -2
    num2 = -1

    result = basic_functions.sub(num1, num2)

    assert result == -1


def test_mult():

    num1 = 2
    num2 = 2

    result = basic_functions.mult(num1, num2)

    assert result == 4


def test_mult_negative():

    num1 = -2
    num2 = -2

    result = basic_functions.mult(num1, num2)

    assert result == 4


def test_div():

    num1 = 4
    num2 = 2

    result = basic_functions.div(num1, num2)

    assert result == 2


def test_div_zero():

    num1 = 4
    num2 = 0

    with raises(ZeroDivisionError) as exinfo:
        basic_functions.div(num1, num2)

    assert str(exinfo.value) == "Can not divide by zero."
