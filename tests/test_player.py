import pytest

from music_tree.player import Player
from music_tree.base.node import *


def test_00_setup():
    assert 1 == 1


# def test_01_play_node():
#     """ Проверка на проигрывание базовой ноды """
#     node = Tempo(60)

#     # TODO: параметризовать, добавить экземпляр ноды каждого типа

#     with Player() as player:
#         player.play(node)
#         # TODO: проверять количество вызовов SoundEngine на соответствие нотам
#         # TODO: stopped станет актуальным, когда вызов плеера станет неблокирующим
#         assert player.stopped == True


@pytest.mark.inProgress
@pytest.mark.sound
def test_04_nonBlockable():
    player = Player()
    node = Chord([0, 3, 10])
    print("ok")
    player.play(node)
    print("good")
    assert player.stopped

@pytest.mark.inProgress
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
