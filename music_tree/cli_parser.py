#!/usr/bin/env python3

""" Парсер из командной строки.
Чтобы упростить ввод, возьмём парсер, отдельный от чтения файла.
"""

import argparse

from music_tree.base.node import *


class CliParser():
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            description='Parse music node arguments')

        subparsers = self.parser.add_subparsers(help='subcommand')

        parser_init = subparsers.add_parser("init")
        parser_pool = subparsers.add_parser("pool")
        parser_track = subparsers.add_parser("track")

        parser_init.add_argument("tempo", help='Base tempo value')
        parser_init.add_argument("name", help='Composition name')

        self.parser.add_argument('name', action='store', help='calling name')

        # TODO: позиционный аргумент - по сути, субпарсер
        # https://habr.com/ru/post/144416/
        self.parser.add_argument(
            '-t', action='store', dest='tempo', help='Tempo value')

    # FIXME: отказ от чистых нод
    def make_node(self, input):
        args = self.parser.parse_args(input)

        if args.tempo != None:
            return Tempo(args.tempo)

        return None

    def parseInput(self, input):
        args = self.parser.parse_args(input)

        print(args)
