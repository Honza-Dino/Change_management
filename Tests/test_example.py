
import pytest
#test OK
def test_number_add():
    x = 1 + 1
    assert x == 2
    assert type(x) == int
#------------------------------------------
 #test NOK
def test_number_subtract():
    y = 6 - 1
    assert y == 0
    assert type(y) == int
#------------------------------------------
# otestování vyjímky 10/0 není 0. Nulou nelze dělit
def test_numbers_divide_zero_throws_exception():
    with pytest.raises(ZeroDivisionError):
        z = 10 / 0
#-------------------------------------------
# Fixtures - připrava pevného zdroje pro různé testování
@pytest.fixture
def data_test_fixture():
    return[1,2,3]

def test_first_element(data_test_fixture):
    assert data_test_fixture[0] == 1


def test_second_element(data_test_fixture):
    assert data_test_fixture[1] == 2

#----------------------------------------------
# Prarametrizace
@pytest.mark.parametrize("first_number, second_number, expected_result", [
    # Testovací scénáře:
    (10, 20, -10),
    (5, 3, 2),
    (10, 3,7),
    (0, 10, -10)
])

def test_number_subtract(first_number, second_number, expected_result):
    actual_result = first_number - second_number
    assert actual_result == expected_result

