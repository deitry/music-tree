""" Принимает на вход ноду, раскрывает её и проигрывает содержимое """

import time
from datetime import datetime
import pyaudio as pa

# TODO: configure instruments/__init__.py
from music_tree.instruments.sin_wave import SinWave
from music_tree.base.node import Timecode, MAX_TICK

MAX_VOICES = 4
# NOTE: при большем количестве голосов слышны помехи на ровном месте
# Надо понять откуда они берутся
DEFAULT_BITRATE = 44100


class Voice():
    """ Принимает байты от звукогенератора и воспроизводит их.
        Один голос - одна нота - один поток. """

    def __init__(self):
        self._buffer = [chr(0)]  # соответственно частоте дискретизации
        # TODO: посмотреть, сколько запрашивается в каллбеке
        # TODO: генераторы вместо фиксированного буфера

        self.running = False
        self.current = 0

    def start(self, pyaudio, bitrate):
        # запуск потока
        self.stream = pyaudio.open(format=pyaudio.get_format_from_width(1),
                                   channels=1,
                                   rate=bitrate,
                                   output=True,
                                   stream_callback=self.callback)

        self.stream.start_stream()
        self.running = True

    def stop(self):
        # остановка потока
        self.running = False
        self.stream.stop_stream()
        self.stream.close()

    def setData(self, data):
        """ Принимаем данные на проигрывание """
        self._buffer = data
        self.current = 0

    def callback(self, in_data, frame_count, time_info, status):
        flag = pa.paContinue
        # if self.running else pa.paComplete
        # complete только по прямому указанию остановиться

        # циклически воспроизводим текущий звук
        data = ''
        for i in range(frame_count):
            # FIXME: переделать на генератор?
            data += self._buffer[self.current]
            self.current += 1
            if self.current >= len(self._buffer):
                self.current = 0

        return (data, flag)


class SoundPool():
    def play(self, sound):
        # запрос на проигрывание звука
        return 0  # возвращаем ид занятого голоса, чтобы знать кого прекращать.
        # вероятно, будет лучше, если это будет инкапсулировано внутри этого же класса

    def stop(self, id):
        pass


class Player():
    def __init__(self, **kwargs):
        self._testMode = kwargs["test"] if "test" in kwargs else True
        self.stopped = True
        self.last = datetime.now()

        self.bitrate = DEFAULT_BITRATE
        self.p = pa.PyAudio()
        self.stream = None

        # TODO:
        self.waveGen = SinWave(self.bitrate)
        # self.instruments = { "sin": SinWave(self.bitrate) }
        self.voices = []

        cnt = MAX_VOICES
        for _ in range(cnt):
            self.voices.append(Voice())

    # NOTE: blockable, but works through non-blockable callback
    def play(self, composition):  # node

        # получаем ноты и "вставляем" в генераторы
        text = composition.texts[0]

        self.stopped = False

        cursor = Timecode(0, 0)
        tempo = 120.
        # TODO: динамический расчёт задержки в зависимости от контекста
        delay = 60. / tempo / MAX_TICK

        VOICE_CNT = len(self.voices)

        REST = self.waveGen.rest()
        activeVoices = 0

        # Заблаговременно находим крайний элемент - когда останавливаться
        lastTimeCode = sorted(list(text.notes.keys()))[-1]
        # print("END AT:", lastTimeCode)

        # Запускаем голоса
        # TODO: В дальнейшем имеет смысл держать по пулу на каждый текст
        # TODO: запускать голоса имеет смысл, когда они на самом деле будут
        # использоваться. До этого можно держать их выключенными
        for voice in self.voices:
            voice.start(self.p, self.bitrate)

        prev = time.localtime()

        while not self.stopped:
            # - для текущего таймкода курсора запрашиваем у всех текстов ноты
            currentNotes = []

            # TODO: обработка "управляющих" символов

            # for text in texts:
            if cursor in text.notes:
                for note in text.notes[cursor]:
                    currentNotes.append(note)

            CUR_CNT = len(currentNotes)

            if CUR_CNT > 0:
                # - если есть - отправляем в потоки
                # Если нот нет, полагаем, что ничего делать не надо
                # TODO: начало пауз будет самостоятельным объектом
                # TODO: с каждым текстом связать свой собственный микропул голосов
                for i in range(CUR_CNT):
                    if i >= VOICE_CNT:
                        break

                    # print("before:", time.ctime())
                    waveData = self.waveGen.toBytes(currentNotes[i])
                    # print("middle:", time.ctime())
                    self.voices[i].setData(waveData)
                    # print("after:", time.ctime())

                # если в прошлый цикл активных голосов было больше, надо их занулить
                if CUR_CNT < activeVoices:
                    for i in range(activeVoices - CUR_CNT):
                        self.voices[CUR_CNT + i].setData(REST)

                        # TODO: стопить потоки неактивных голосов

                activeVoices = min(CUR_CNT, MAX_VOICES)

            # DEBUG:
            # new = time.localtime()
            # print(delay, cursor, time.asctime(new), new.tm_sec - prev.tm_sec)
            # prev = new

            # - sleep() согласно текущему темпу
            time.sleep(delay)

            # - переходим на следующий шаг тика
            cursor.incTick()

            # если достигли крайнего элемента - выходим
            if cursor >= lastTimeCode:
                self.stopped = True

        # terminate streams
        for voice in self.voices:
            voice.stop()

        # FIXME: call in destructor
        self.p.terminate()
