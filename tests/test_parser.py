import pytest

from music_tree.parser import Parser

def test_00_setup():
    assert 1 == 1

@pytest.mark.skip
def test_01_parser_read_file():
    parser = Parser()
    try:
        node = parser.make_node("resources/test_node.mun")
        # FIXME: проверка на соответствие ноды задуманному
        assert False

    except:
        pytest.fail("parser did not make it...")
