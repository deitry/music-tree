""" Интеграционное тестирование main """

import pytest

from main import main


def test_00_basic_setup():
    assert 1 == 1


@pytest.mark.parametrize(
    ("input"),
    [
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
        (['link', 'intro', '3', 'word1', '1']), # link snap #3 of intro and snap #1 of word1
        # "mt insert intro 1 '1^ 2 3^'" # insert into text anonymous word.
        # # - link on 1 snappoint of intro and #1 snappoint of word
        # "mt insert intro 1 '1^ 2 3^' 2" # insert into text anonymous word
        # # - link on 1 snappoint of intro and #2 snappoint of word
        # # "mt link intro 5 word1 2", # ERROR: no such snap in word1

        (['play']), # WARNING: no content in composition
        (['track', '--rename', 'track1', 'skeleton']), # edit parameters of tracks
        # # - composition initialized with 8 (by default) tracks

        # # markers
        (['marker', '0', '0', 'begin']), # insert marker
        (['marker', '4', '0', 'action']),
        (['marker', '--list']), # list all named markers
        (['marker', '--all']), # list all snappoints including beats and other

        # # link text and track
        # # "mt link track1 0 intro", # ERROR: no such track or text
        (['link', 'skeleton', '1', 'intro', '1']),
    ])
def test_01_single_line_parse(input):
    """ Простой запуск main с единичной нодой """
    print(input)
    main(input)


#TODO: запуск main должен выполнять CliParser.parse(argv) + Player.play(node)
