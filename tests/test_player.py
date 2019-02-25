import pytest

from music_tree.player import Player
from music_tree.base.node import *


def test_00_setup():
    assert 1 == 1


def test_01_play_node():
    """ Проверка на проигрывание базовой ноды """
    node = Tempo(60)

    # TODO: параметризовать, добавить экземпляр ноды каждого типа

    with Player() as player:
        player.play(node)
        # TODO: проверять количество вызовов SoundEngine на соответствие нотам
        # TODO: stopped станет актуальным, когда вызов плеера станет неблокирующим
        assert player.stopped == True

@pytest.mark.sound
def test_02_testPlay():
    implPlay(False)

@pytest.mark.sound
@pytest.mark.env("sound")
def test_03_testPlayWithSound():
    implPlay(True)

def implPlay(needSound):
    try:
        testSound = needSound

        with Player(test=not testSound) as pl:
            pl.testPlay(0, 0.2)
            pl.testPlay(15, 0.2)
            pl.testPlay(14, 0.2)
            pl.testPlay(10, 0.2)
            pl.testPlay(12, 0.8)
            pl.testPlay(14, 0.4)
            pl.testPlay(7, 0.4)
            pl.testPlay(10, 0.8)

            pl.testPlay(12, 0.27)
            pl.testPlay(13, 0.27)
            pl.testPlay(12, 0.27)
            pl.testPlay(0, 0.8)
    except BaseException:
        print("Something goes wrong")

@pytest.mark.inProgress
@pytest.mark.sound
def test_04_nonBlockable():
    player = Player()
    node = Chord()
    print("ok")
    player.play(node)
    print("good")
    assert player.stopped
