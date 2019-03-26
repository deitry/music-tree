# import pytest
from music_tree.base.composition import Symbol, Word, Text


def test_word():

    word = Word()
    word.symbols.append(Symbol(1))
    word.symbols.append(Symbol(2))
    word.symbols.append(Symbol(3))
    word.symbols.append(Symbol(1))

    # для простоты
    word.symbols[0].accent = True
    word.symbols[2].accent = True

    text = Text()
    # 1. Добавляем
    text.addLink()


def test_text():
    text = Text()

    # TODO: вставка слова в текст с привязкой к конкретным snappoints
