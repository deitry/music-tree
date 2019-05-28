""" Базовый класс для музыкальной ноды """


class Node():
    def __init__(self):
        pass


MAX_TICK = 32


class Timecode():
    def __init__(self, beat, tick):
        self.beat = beat
        self.tick = tick

# пока я не придумал, какая между ними всеми должна быть взаимосвязь,
# все накидаю в единый файлик


# ноты:
# BEAT  TICK    VALUE
# 0     0       0
# 1     0       3
# 1     16      7


class Context():
    """ Для конкретизации: хранить в нём текущую гармонию, темп ... """
    pass


class SingleText():
    """ Сопоставление таймкодов и нот/нод. """

    # с одиночной партией напрямую не очень удобно работать.
    # В качестве главного элемента имеет смысл использовать Text просто,
    # а на отдельные голоса разбивать автоматически. Тогда можно будет спокойно
    # использовать аккорды

    def __init__(self):
        # NOTE: попробуем на основе дикта вместо списка пар таймкод-значение
        self.notes = dict()
        self.last = Timecode(0, 0)

    def add(self, timecode, node):
        # NOTE: подразумеваем возможность размещать в данной точке любую ноду.
        # С учётом того, что в качестве ноды может выступать слово с ударением не на первой ноте,
        # фактическое начало ноды может быть раньше.
        self.notes[timecode] = node

    def concretize(self):
        """ Вовзращает словарь из нот - все ноды уже "развёрнуты" """
        return dict()


class Tempo():
    def __init__(self, tempo):
        self.tempo = float(tempo)

    def __eq__(self, other):
        if isinstance(other, Tempo):
            return self.tempo == other.tempo

        return False

    def getNotes(self):
        period = 60 / self.tempo
        activeLen = period * 0.25
        inactiveLen = period - activeLen  # добавляем паузы
        notes = [
            note for i in range(8)
            for note in [(12, activeLen), (-200, inactiveLen)]
        ]
        return notes


class TimeSignature():
    def __init__(self):
        self.numenator = 3
        self.denumenator = 4


class Chord():
    def __init__(self, notes):
        self.baseNote = 0
        self.notes = notes
        # TODO: ChordBuilder ?
        # = ChordBuilder(description)

    def getNotes(self):
        return [(note, 1) for note in self.notes]

    # def concretize(self, context):
    #     return

class Rhythm():
    def __init__(self, line):
        self.line = line  # в качестве линии идут символы [10.]
        self.multiplier = 1  # какой длительности соответствует единичный символ
        # 1 -> четверть


class Sequence():
    def __init__(self, line):
        # line вида 1 3 5 3 7 3 5
        # длину будем учитывать другой нодой?
        self.line = line


class Rest():
    """ Просто пауза """

    def __init__(self):
        self.length = 1


class HorizontalLayout():
    """ Объединяет несколько нод в линейную последовательность """

    def __init__(self):
        self.nodes = []


class VerticalLayout():
    """ Объединяет несколько нод "по вертикали" """

    def __init__(self):
        self.nodes = []


class Agregate():
    """ Объединяет несколько нод в одну в одном и том же месте.
    Например, из ритма и последовательности нот делает мелодию """
    pass
