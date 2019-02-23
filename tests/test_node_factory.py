import pytest

from music_tree.node_factory import NodeFactory

def test_00_setup():
    assert 1 == 1

@pytest.mark.skip("Not implemented")
@pytest.mark.parametrize(("nodeType", "input"),
[
    # FIXME: что-то вроде енама вместо целочисленного типа
    # TODO: значения аргументов брать те же, что и для тестирования CliParser?
    (1, "100100100"), # ритм
    (1, "100.10..1.0."), # ритм
    (2, "1343"), # generic
    (3, "am dm em"), # chords
])
def test_01_create_node(nodeType, input):
    factory = NodeFactory()
    try:
        node = factory.create_node(nodeType, input)
        # FIXME: проверка на соответствие ноды задуманному
        raise NotImplementedError

    except:
        pytest.fail("parser did not make it...")
