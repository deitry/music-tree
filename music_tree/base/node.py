""" Базовый класс для музыкальной ноды """

class Node():

    def __init__(self):
        pass

# пока я не придумал, какая между ними всеми должна быть взаимосвязь,
# все накидаю в единый файлик

class Tempo():
    def __init__(self):
        self.tempo = 120

class TimeSignature():
    def __init__(self):
        self.numenator = 3
        self.denumenator = 4

class Chord():
    def __init__(self, description):
        self.baseNote = 0 # == A
        self.notes = [0, 3, 7] # = 1+3+5 = minor
        # TODO: ChordBuilder ?
        # = ChordBuilder(description)

class Rhythm():
    def __init__(self, line):
        self.line = line # в качестве линии идут символы [10.]
        self.multiplier = 1 # какой длительности соответствует единичный символ
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
