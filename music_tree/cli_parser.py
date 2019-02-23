""" Парсер из командной строки.
Чтобы упростить ввод, возьмём парсер, отдельный от чтения файла.
"""

import argparse

from music_tree.base.node import *


class CliParser():
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            description='Parse music node arguments')
        self.parser.add_argument('name', action='store', help='calling name')

        # TODO: позиционный аргумент - по сути, субпарсер
        # https://habr.com/ru/post/144416/
        self.parser.add_argument(
            '-t', action='store', dest='tempo', help='Tempo value')

    def make_node(self, input):
        args = self.parser.parse_args(input)

        if args.tempo != None:
            return Tempo(args.tempo)

        return None
