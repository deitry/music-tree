# Будет использоваться в качестве точки входа

# Алгоритм работы:
# - в папке (с вложенными папками) держим файлы нод.
# - - нода может содержать в себе конкретные ноты,
# - - а может включать другие ноды
# - создать можно командой
# - - mut create node.mun
# - - - mut - от MUsic Tree
# - - - mun - MUsic Node
# - - Предполагается, что создав таким образом, можно слегка упростить
#     жизнь за счёт темплейтов
# - - Идея разбиения на ноды в отдельных файлах в том, чтобы можно было
#     было версифицировать гитом и проще переносить из проекта в проект
# - - Редактор тоже консольный?
# - передаём одну из нод на вход в программу:
# - - mut play node.mun
# - PROFIT !!

from music_tree.cli_parser import CliParser
from music_tree.player import Player

def main(argv=None):
    parser = CliParser()

    args = parser.parseInput(argv)

#     with Player() as player:
#         player.play(node)

if __name__ == '__main__':
    main()
