from src.keybord import Keyboard

kb = Keyboard('Dark Project KD87A', 9600, 5)

def test_keyboard():
    assert type(kb.name) == str


def test_change_lang():
    kb.change_lang()
    assert kb.language == "RU"
    kb.change_lang()
    assert kb.language == "EN"

