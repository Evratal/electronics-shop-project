from src.item import Item


class MixinLangChang():
    __language = "EN"

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"



class Keyboard(Item, MixinLangChang):
    pass


kb = Keyboard('Dark Project KD87A', 9600, 5)
print(kb.language)
kb.change_lang()
