import pytest

from music_tree.base.text import *

def test_00_setup():
    assert 0 == 0

def test_01_basic_word():
    w1 = Word([0,2,3])

    assert w1.strike == 0
    assert w1.tempo == 1
    assert w1.getNote(Timecode(0, 0), Timecode(0, 0)) == 0
