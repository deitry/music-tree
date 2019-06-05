""" Файл с примерами небольших текстов """

# FIXME: все проекты должны быть легко запускаемыми, но делать их тестами не стоит

import pytest

from music_tree.player import Player
from music_tree.base.composition import Composition
from music_tree.base.timecode import Timecode



def test_00_setup():
    assert 1 == 1

@pytest.mark.sound
def test_01_metronome():
    player = Player()
    main = Composition()
    root = main.texts[0]

    root.add(Timecode(0, 0), [24])
    root.add(Timecode(0, 4), [0])
    root.add(Timecode(1, 0), [24])
    root.add(Timecode(1, 4), [0])
    root.add(Timecode(2, 0), [24])
    root.add(Timecode(2, 4), [0])
    root.add(Timecode(3, 0), [24])
    root.add(Timecode(3, 4), [0])
    root.add(Timecode(4, 0), [24])
    root.add(Timecode(4, 4), [0])

    # отдельным объектом обозначаем конец текста
    root.add(Timecode(5, 0), 0)

    player.play(main)
    assert player.stopped
