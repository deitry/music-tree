""" Интеграционное тестирование main """

import pytest

from main import main


def test_00_basic_setup():
    assert 1 == 1


@pytest.mark.parametrize(
    ("input"),
    [
        # "r 100100100", # ритм
        # "r 100.10..1.0.", # ритм
        # "g 1343", # generic
        # "c am dm em", # chords
        (["", "-t", "120"]),
    ])
def test_01_basic_node(input):
    """ Простой запуск main с единичной нодой """

    main(input)


#TODO: запуск main должен выполнять CliParser.parse(argv) + Player.play(node)
