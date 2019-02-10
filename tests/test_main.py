from music_tree.base.note_node import NoteNode


def test_00_basic_setup():
    assert 1 == 1

def test_01_nodw_init():
    node = NoteNode()
    assert node.value == 0
