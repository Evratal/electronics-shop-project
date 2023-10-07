import csv


from src.instantiateCSVError import InstantiateCSVError


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    path_file = "../src/items.csv"

    def __init__(self, name: str, price: float, quantity: int):
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.path_file = self.path_file
        super().__init__()

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self):
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * Item.pay_rate
        return self.price

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    @property
    def name(self):
        """Геттер.Возвращает имя"""
        return self.__name

    @classmethod
    def instantiate_from_csv(cls, number=1, path=path_file):
        """Открываем файл и проверяем на его"""
        try:
            with open(path, encoding="utf-8") as file:

                dict_csv = csv.DictReader(file)
                len_field_dict = len(dict_csv.fieldnames)
                dict_used = [] #создаем словарь, куда будем записывать строчки из файла, для дальнешй с ними работы
                if len_field_dict !=3:
                    raise InstantiateCSVError('InstantiateCSVError: Файл item.csv поврежден')
                for el in dict_csv:
                    dict_used.append(el)

                    """С помощью number выбираем товар из списка (проверяем, чтобы номер не выходил за список)"""

                    if number < 1 or number > 5:
                        number = 1
                    name = dict_used[number - 1]["name"]
                    price = int(dict_used[number - 1]["price"])
                    quantity = int(dict_used[number - 1]["quantity"])

        except FileNotFoundError:
            print("FileNotFoundError: Отсутствует файл item.csv")
            raise
        except InstantiateCSVError:
            print('InstantiateCSVError: Файл item.csv поврежден')
            raise
        return cls(name, price, quantity)

    @staticmethod
    def string_to_number(string):
        number = int(string)
        return number

    @name.setter
    def name(self, name):
        """Сеттер. Меняет имя"""
        if len(name) <= 10:
            self.__name = name
        else:
            self.__name = name[:10]

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только Item и дочерние от них Phone.')
        return int(self.quantity) + int(other.quantity)
