class Timecode():
    """ Класс, определяющий точное местоположение на таймлайне композиции.

        Точность обеспечивается указанием доли и "дробной" части.
        Актуально для событий управляющих дорожек, предполагается,
        что события на "музыкальных" дорожках будут проецироваться на таймлайн
        с помощью точек привязки. """

    def __init__(self, beat=0, tick=0):
        self.beat = int(beat)
        self.tick = int(tick)

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Timecode):
            return self.beat == other.beat and self.tick == other.tick
        return False


class Snap():

    def __init__(self, name, source):
        # в первом приближении точка привязки определяется только именем
        # и таймкодом расположения
        self.name = name
        self.source = source


class TimeSnap(Snap):

    def __init__(self, name, source, timecode):
        # в первом приближении точка привязки определяется только именем
        # и таймкодом расположения
        Snap.__init__(self, name, source)
        self.timecode = timecode


class Link():
    """ Связь между двумя точками привязки.

    Первая точка берётся у объекта, вторая - у контейнера, в который
    объект вкладывается. NOTE: на момент создания связь скорее всего валидна.
    Но в результате редатктирования объекта или контейнера исходные точки
    привязки могут пропасть. Необходимо регулярно проверять на валидность """

    def __init__(self, objectSnap, containerSnap):
        self.objectSnap = objectSnap
        self.containerSnap = containerSnap


class Symbol():
    """ Одиночный символ в музыкальном слове """

    def __init__(self, value=0):
        # self.type = 0  # на случай не только нот
        self.value = value
        self.accent = False  # "ударение", которое сделает его точкой привязки


class Word():
    """ Одиночное "музыкальное слово".

    У слова должна быть по меньшей мере одна точка привязки. """

    # Представим себе такое: (галочкой отмечено "ударение", т.е. out_snappoint)
    # 1^ 2 3^ 1
    # Представим, что

    def __init__(self):
        self.symbols = []  # символы, из которых состоит слово
        # - только конкретные ноты, их расположение на конечном таймлайне
        # зависит от настройки точек привязки и "управляющих значений"

    def out_snaps(self):
        """ Получает набор текущих точек привязки """
        pass

class Text():
    """ Класс, определяющий одну набор музыкальных слов, т.е. фразу.

    Подобно словам в тексте, текст располагается внутри композиции с помощью
    точек привязки. """

    def __init__(self):

        # события - список пар [cursor(start_time), event_obj]
        # TODO: именованные snappoints?! по типу функций
        # TODO: неймспейсы для snappoints? A.start, A.a.end

        # self.events = []
        # self.snappoints = []  # хранить только вручную добавленные,
        # те, что генерируются на лету (e.g. начало такта), хранить нет смысла

        self.links = []

        pass

    def addLink(self, link):
        self.links.append(link)

class Composition():
    """ Класс, объединяющий в себе всю информацию про композицию """

    def __init__(self):

        # управляющие дорожки:
        # - markers
        # - tempo
        # - time signature
        # - scale
        # - harmony
        # - harmony
        # - dynamics
        # - snappoints < генерируемые на основе signature плюс generic notes

        pass
