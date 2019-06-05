import pytest

from music_tree.player import Player
# from music_tree.base.composition import Composition
# from music_tree.base.timecode import Timecode
# from music_tree.base.node import *
from music_tree.base import *


def test_00_setup():
    assert 1 == 1


@pytest.mark.sound
def test_04_nonBlockable():
    player = Player()
    main = Composition()
    root = main.texts[0]
    root.add(Timecode(0, 0), [-24, -11, 0])
    root.add(Timecode(5, 0), 0)

    player.play(main)

    assert player.stopped


@pytest.mark.sound
def test_05_nodes():
    player = Player()
    main = Composition()
    root = main.texts[0]

    root.add(Timecode(0, 0), [0, 7, 12])
    root.add(Timecode(1, 0), [3, 10])
    root.add(Timecode(3, 0), [0, 15])
    # отдельным объектом обозначаем конец текста
    root.add(Timecode(5, 0), 0)

    player.play(main)
    assert player.stopped
