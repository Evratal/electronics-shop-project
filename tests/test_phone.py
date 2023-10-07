import pytest

from src.phone import Phone
from src.item import Item


# def test_calculate_total_price():
#     assert phone1.calculate_total_price() == 1200000

@pytest.fixture()
def nout():
    return Item("Ноутбуки", 20000, 100)

@pytest.fixture()
def phone1():
    return Phone("Redmi", 12000, 100, 80)


def test_add(phone1,nout):
    assert phone1 + nout == 200