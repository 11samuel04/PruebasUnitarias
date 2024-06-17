import pytest
from main import sum, es_mayor_que, login

def test_sum():
    assert sum(2,5) == 7
    print("La funcion suma1 trabaja correctamente")
    
def test_sum2():
    assert sum(4, 6) == 10
    print("La funcion suma2 trabaja correctamente")
    
def test_es_mayor_que():
    assert es_mayor_que(10, 2)
    print("La funcion es mayor que trabaja correctamente")

def test_login_pass():
    login_passes = login("Metodologia", "710011C")
    assert login_passes
    
def test_login_fail():
    login_fails = login("Metodologias", "710012C")
    assert not login_fails