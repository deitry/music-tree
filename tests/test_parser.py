import pytest

from music_tree.parser import Parser

def test_00_setup():
    assert 1 == 1

def test_01_parser_read_file():
    parser = Parser()
    try:
        node = parser.make_node("resources/test_node.mun")
    except:
        pytest.fail("parser did not make it...")

