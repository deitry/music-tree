""" Описания различных струкурных составляющих. """


class Context():
    """ Для конкретизации: хранить в нём текущую гармонию, темп ... """
    pass


class Node():
    """ Базовый класс для музыкальной ноды """

    def __init__(self):
        pass


class Chord(Node):
    def __init__(self, notes):
        # TODO: у всех нод доступ к нотам должен быть одинаков
        self.notes = notes


class Tempo():
    # TODO: На подумать: как можно реализовать область переменного темпа?
    # Например, плавное ускорение или рандомизацию

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
