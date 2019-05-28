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
    node = Chord()
    print("ok")
    player.play(node)
    print("good")
    assert player.stopped
