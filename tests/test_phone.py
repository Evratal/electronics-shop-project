from src.phone import Phone
from src.item import Item


phone1 = Phone("Redmi", 12000, 100, 80)
nout = Item("Ноутбуки", 20000, 100)

# def test_calculate_total_price():
#     assert phone1.calculate_total_price() == 1200000

def test_add():
    assert phone1 + nout == 200