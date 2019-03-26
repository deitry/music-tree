import pytest

from music_tree.cli_parser import CliParser
from music_tree.base.node import Tempo

def test_00_setup():
    assert 1 == 1

@pytest.mark.parametrize(("input", "result"),
[
    # "r 100100100", # ритм
    # "r 100.10..1.0.", # ритм
    # "g 1343", # generic
    # "c am dm em", # chords
    (["", "-t", "120"], Tempo(120)),
])
def test_01_parser_read_file(input, result):
    parser = CliParser()
    node = parser.make_node(input)

    # проверка на соответствие ноды задуманному
    assert node == result


@pytest.fixture()
def mockProjectInput():
    """ Влажные мечты о том, как должна происходить работа над проектом. """

    lines = [
        # init composition
        "mt init",

        # add into pool
        # ? "mt pool add word '1 2 3^'", # anonymous word
        "mt pool --add word '1 2^ 3' word1", # named word
        "mt pool --add word '1 2^ 1 3^' main_word", # word with two accents
        "mt pool --add text intro", # named text. Anonymous texts is not permitted

        # link text and word
        "mt link intro 3 word1 1", # link snap #3 of intro and snap #1 of word1
        "mt insert intro 1 '1^ 2 3^'" # insert into text anonymous word.
        # - link on 1 snappoint of intro and #1 snappoint of word
        "mt insert intro 1 '1^ 2 3^' 2" # insert into text anonymous word
        # - link on 1 snappoint of intro and #2 snappoint of word
        # "mt link intro 5 word1 2", # ERROR: no such snap in word1

        "mt play", # WARNING: no content in composition
        "mt track --rename track1 skeleton", # edit parameters of tracks
        # - composition initialized with 8 (by default) tracks

        # markers
        "mt marker 0 0 begin", # insert marker
        "mt marker 4 0 action1",
        "mt marker --list" # list all named markers
        "mt marker --all" # list all snappoints including beats and other

        # link text and track
        # "mt link track1 0 intro", # ERROR: no such track or text
        "mt link skeleton "
    ]
    return lines


@pytest.mark.skip("thinking of")
def test_10_project(mockProjectInput):
    parser = CliParser()
    for line in input:
        parser.parse(line)
