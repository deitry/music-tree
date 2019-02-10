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
    except:
        pytest.fail("player did not make it...")

