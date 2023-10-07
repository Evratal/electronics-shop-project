import pytest

from src.keybord import Keyboard


@pytest.fixture()
def kb():
    return Keyboard('Dark Project KD87A', 9600, 5)

def test_keyboard(kb):
    assert type(kb.name) == str


def test_change_lang(kb):
    kb.change_lang()
    assert kb.language == "RU"
    kb.change_lang()
    assert kb.language == "EN"

