""" Описания различных струкурных составляющих. """

MAX_TICK = 32


class Timecode():
    def __init__(self, beat, tick):

        self.beat = max([beat, 0])
        self.tick = min([max([tick, 0]), MAX_TICK])

    def incTick(self):

        self.tick += 1
        if self.tick >= MAX_TICK:
            self.tick = 0
            self.beat += 1

    def dec(self):
        self.tick -= 1
        if self.tick < 0:
            self.tick = MAX_TICK - 1
            self.beat -= 1

    def __gt__(self, other):
        if isinstance(other, Timecode):
            return any([
                self.beat > other.beat, self.beat == other.beat
                and self.tick > other.tick
            ])
        return False

    def __ge__(self, other):
        if isinstance(other, Timecode):
            return any([
                self.beat > other.beat, self.beat == other.beat
                and self.tick >= other.tick
            ])
        return False

    def __lt__(self, other):
        if isinstance(other, Timecode):
            return any([
                self.beat < other.beat, self.beat == other.beat
                and self.tick < other.tick
            ])
        return False

    def __eq__(self, other):
        if isinstance(other, Timecode):
            return all([self.beat == other.beat, self.tick == other.tick])
        return False

    def __repr__(self):
        return str(self.beat) + ":" + str(self.tick)

    def __hash__(self):
        return hash((self.beat, self.tick))


class Context():
    """ Для конкретизации: хранить в нём текущую гармонию, темп ... """
    pass


class Text():
    """ Сопоставление таймкодов и нот/нод. """

    # с одиночной партией напрямую не очень удобно работать.
    # В качестве главного элемента имеет смысл использовать Text просто,
    # а на отдельные голоса разбивать автоматически. Тогда можно будет спокойно
    # использовать аккорды

    # В составе текста нужно располагать не отдельные ноты-точки, а области,
    # у которых нужно запрашивать, не хотят ли они что-то добавить в данный момент
    # NOTE: Напрашивается некая параллель с рейтрейсингом.

    def __init__(self):
        # NOTE: попробуем на основе дикта вместо списка пар таймкод-значение
        self.notes = dict()
        self.last = Timecode(0, 0)

    def add(self, timecode, node):
        # NOTE: подразумеваем возможность размещать в данной точке любую ноду.
        # С учётом того, что в качестве ноды может выступать слово с ударением не на первой ноте,
        # фактическое начало ноды может быть раньше - реализация слов
        self.notes[timecode] = node

    def concretize(self):
        """ Вовзращает словарь из нот - все ноды уже "развёрнуты" """
        return dict()


class Composition():
    def __init__(self):
        self.texts = [Text()]

        # TODO:
        # - texts - собственно наполнение
        # - controlText - специально выделенный текст с управляющими символами.
        # Для бОльших игр с динамикой имеет смысл рассчитывать,
        # что в управляющей дорожке будут не только одиночные символы
        # Для обычных дорожек тоже имеет смысл обдумать возможность использования
        # не-точечных объектов


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
