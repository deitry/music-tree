import pytest

from music_tree.cli_parser import CliParser

def test_00_setup():
    assert 1 == 1

@pytest.mark.parametrize("input",
[
    "r 100100100", # ритм
    "r 100.10..1.0.", # ритм
    "g 1343", # generic
    "c am dm em", # chords
])
def test_01_parser_read_file(input):
    parser = CliParser()
    try:
        node = parser.make_node(input)
        # FIXME: проверка на соответствие ноды задуманному
        assert False

    except:
        pytest.fail("parser did not make it...")
