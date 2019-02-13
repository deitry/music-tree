from music_tree.base.note_node import NoteNode


def test_00_basic_setup():
    assert 1 == 1

def test_01_node_init():
    node = NoteNode()
    raise NotImplementedError

#TODO: запуск main должен выполнять CliParser.parse(argv) + Player.play(node)
