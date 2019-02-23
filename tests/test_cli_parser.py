import pytest

from music_tree.cli_parser import CliParser
from music_tree.base.node import Tempo

def test_00_setup():
    assert 1 == 1

@pytest.mark.parametrize(("input", "result"),
[
    # "r 100100100", # ритм
    # "r 100.10..1.0.", # ритм
    # "g 1343", # generic
    # "c am dm em", # chords
    (["", "-t", "120"], Tempo(120)),
])
def test_01_parser_read_file(input, result):
    parser = CliParser()
    node = parser.make_node(input)

    # проверка на соответствие ноды задуманному
    assert node == result
