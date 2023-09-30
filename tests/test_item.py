"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

nout = Item("Ноутбуки", 20000, 100)


def test_calculate_total_price():
    assert nout.calculate_total_price() == nout.price * nout.quantity


def test_apply_discount():
    assert nout.apply_discount() == nout.price * Item.pay_rate


def test_name():
    assert nout.name == "Ноутбуки"
    nout.name = "Игровой ноутбук Thunderobot"
    assert nout.name == "Игровой но"


def test_instantiate_from_csv():
    new_item = Item.instantiate_from_csv(1)
    assert isinstance(new_item, Item)
    assert new_item.name == "Смартфон"
    assert new_item.price == 100
    assert new_item.quantity == 1


def test_string_to_number():
    assert Item.string_to_number("100") == 100


nout_1 = Item("Ноутбуки", 20000, 100)


def test_str():
    assert str(nout_1) == 'Ноутбуки'


def test_repr():
    assert repr(nout_1) == "Item('Ноутбуки', 20000, 100)"


def test_add():
    assert nout_1 + nout == 200
