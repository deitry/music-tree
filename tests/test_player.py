import pytest

from music_tree.player import Player
from music_tree.base.node import Node

def test_00_setup():
    assert 1 == 1

def test_01_play_node():
    player = Player()
    node = Node()
    try:
        player.play(node)
        assert player.stopped == False
        # проверять количество вызовов SoundEngine на соответствие нотам
    except:
        pytest.fail("player did not make it...")

@pytest.mark.sound
def test_02_testPlay():
    try:
        with Player() as pl:
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
    except AttributeError:
        print(1)

        # player.testPlay(12, 1)
        # player.testPlay(0, 1)
        # player.testPlay(12, 1)
        # player.testPlay(0, 1)
        # player.testPlay(12, 1)
        # player.testPlay(0, 1)


        # player.testPlay(12, 0.125)
        # player.testPlay(12, 0.125)
        # player.testPlay(12, 0.125)
        # player.testPlay(12, 0.125)
        # player.testPlay(0, 0.125)
        # player.testPlay(0, 0.125)
        # player.testPlay(0, 0.125)
        # player.testPlay(0, 0.125)
