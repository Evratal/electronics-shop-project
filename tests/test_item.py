"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

nout = Item("Ноутбуки", 20000, 100)


def test_calculate_total_price():
    assert nout.calculate_total_price() == nout.price * nout.quantity
