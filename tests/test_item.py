"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.instantiateCSVError import InstantiateCSVError
from src.item import Item



@pytest.fixture()
def nout():
    return Item("Ноутбуки", 20000, 100)

def test_calculate_total_price(nout):
    assert nout.calculate_total_price() == nout.price * nout.quantity


def test_apply_discount(nout):
    assert nout.apply_discount() == nout.price * Item.pay_rate


def test_name(nout):
    assert nout.name == "Ноутбуки"
    nout.name = "Игровой ноутбук Thunderobot"
    assert nout.name == "Игровой но"


def test_instantiate_from_csv():
    new_item = Item.instantiate_from_csv(1)
    assert isinstance(new_item, Item)
    assert new_item.name == "Смартфон"



def test_string_to_number():
    assert Item.string_to_number("100") == 100

@pytest.fixture()
def nout_1():
    return Item("Ноутбуки", 20000, 100)


def test_str(nout_1):
    assert str(nout_1) == 'Ноутбуки'


def test_repr(nout_1):
    assert repr(nout_1) == "Item('Ноутбуки', 20000, 100)"


def test_add(nout_1,nout):
    assert nout_1 + nout == 200

def test_FileNotFoundError():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv(1,"321.txt")
def test_InstantiateCSVError():
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv(1,"../src/items_1.csv")