#!/usr/bin/env python3
""" Парсер из командной строки.
Чтобы упростить ввод, возьмём парсер, отдельный от чтения файла.
"""

import argparse

# from music_tree.base.node import *


class CliParser():
    def __init__(self):
        # https://habr.com/ru/post/144416/

        self.parser = argparse.ArgumentParser(
            description='Parse music node arguments')

        self.parser.add_argument(
            '-v',
            '--verbose',
            dest='verbose',
            action='count',
            help='verbose output')
        subparsers = self.parser.add_subparsers(
            help='subcommand', dest='command')

        # по парсеру на каждую субкоманду
        parserInit = subparsers.add_parser("init")  # инициализация композиции
        parserPool = subparsers.add_parser("pool")  # субкоманды пула
        parserLink = subparsers.add_parser(
            "link")  # создать связь (слово-текст)
        parserPlay = subparsers.add_parser("play")  # проиграть композицию
        parserMarker = subparsers.add_parser("marker")  # управление маркерами

        # init
        # FIXME: имя не нужно? брать у текущей папки?
        # или разрешить несколько композиций в одной папке?
        # У них может быть общий пул
        parserInit.add_argument("name", help='Composition name')
        parserInit.add_argument(
            "tempo", nargs="?", type=int, help='Base tempo value', default=120)

        # pool
        poolSubparsers = parserPool.add_subparsers(
            help='pool subcommands', dest='pool_command')

        # pool add
        parserPoolAdd = poolSubparsers.add_parser("add")
        poolAddSubparsers = parserPoolAdd.add_subparsers(
            help="container type", dest='container_type')

        parserPoolAddText = poolAddSubparsers.add_parser("text")
        parserPoolAddWord = poolAddSubparsers.add_parser("word")

        parserPoolAddText.add_argument('name')

        parserPoolAddWord.add_argument('content')
        parserPoolAddWord.add_argument('name')

        # pool rm
        parserPoolRm = poolSubparsers.add_parser("rm")

        # pool play
        parserPoolPlay = poolSubparsers.add_parser("play")

        # link
        parserLink.add_argument('container_name')
        parserLink.add_argument('cont_snap_name')
        parserLink.add_argument('object_name')
        parserLink.add_argument('obj_snap_name')

        # marker
        # parserMarker.add_argument('track_name')
        # markerSubparsers = parserMarker.add_subparsers(
        #     help='marker subcommands', dest='marker_command')
        # markerListParser = markerSubparsers.add_parser("list")

        parserMarker.add_argument('beat', type=int)
        parserMarker.add_argument('tick', type=int)
        parserMarker.add_argument('marker_name')

        # play
        parserMarker.add_argument('start_marker', nargs='?')

    def parseInput(self, argv=None):
        args = self.parser.parse_args(
        ) if argv is None else self.parser.parse_args(argv)

        print(args)
