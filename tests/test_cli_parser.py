import pytest

from music_tree.cli_parser import CliParser
from music_tree.base.node import Tempo

def test_00_setup():
    assert 1 == 1

# @pytest.mark.parametrize(("input", "result"),
# [
#     # "r 100100100", # ритм
#     # "r 100.10..1.0.", # ритм
#     # "g 1343", # generic
#     # "c am dm em", # chords
#     (["", "-t", "120"], Tempo(120)),
# ])
# def test_01_parser_read_file(input, result):
#     parser = CliParser()
#     node = parser.make_node(input)

#     # проверка на соответствие ноды задуманному
#     assert node == result


@pytest.fixture()
def mockProjectInput():
    """ Влажные мечты о том, как должна происходить работа над проектом. """

    # FIXME: дублирование в test_main.py
    lines = [
        # init composition
        (["init", "vobla"]),

        # add into pool
        # ? "mt pool add word '1 2 3^'", # anonymous word
        (['pool', 'add', 'word', "'1 2^ 3'", "word1"]),  # named word
        (['pool', 'add', 'word', "'1 2^ 1 3^'", "word1"
          ]),  # word with two accents
        (['pool', 'add', 'text', "intro"
          ]),  # named text. Anonymous texts is not permitted

        # # link text and word
        # (['link', 'intro', '3', 'word1', '1']), # link snap #3 of intro and snap #1 of word1

        (['play']), # WARNING: no content in composition
        # (['track', '--rename', 'track1', 'skeleton']), # edit parameters of tracks
        # # - composition initialized with 8 (by default) tracks

        # # markers
        # (['marker', '0', '0', 'begin']), # insert marker
        # (['marker', '4', '0', 'action']),
        # (['marker', '--list']), # list all named markers
        # (['marker', '--all']), # list all snappoints including beats and other

        # # link text and track
        # # "mt link track1 0 intro", # ERROR: no such track or text
        # (['link', 'skeleton', '1', 'intro', '1']),
    ]
    return lines


# @pytest.mark.skip("thinking of")
def test_10_project(mockProjectInput):
    parser = CliParser()
    for args in mockProjectInput:
        parser.parseInput(args)
