""" Принимает на вход ноду, раскрывает её и проигрывает содержимое """

import time
from datetime import datetime
import pyaudio as pa

# TODO: configure instruments/__init__.py
from music_tree.instruments.sin_wave import SinWave
from music_tree.base.node import Timecode

# from music_tree.instruments.triangle_wave import TriangleWave
# from music_tree.instruments.square_wave import SquareWave


class Voice():
    """ Принимает байты от звукогенератора и воспроизводит их.
        Один голос - одна нота - один поток. """

    def __init__(self):
        self._buffer = [] # соответственно частоте дискретизации
        # TODO: посмотреть, сколько запрашивается в каллбеке
        # TODO: генераторы вместо фиксированного буфера

        self.running = False
        self.current = 0

    def start(self, pyaudio, bitrate):
        # запуск потока
        self.stream = pyaudio.open(
            format=pyaudio.get_format_from_width(1),
            channels=1,
            rate=bitrate,
            output=True,
            stream_callback=self.callback
        )

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


MAX_VOICES = 6
DEFAULT_BITRATE = 44100


class SoundPool():

    def play(self, sound):
        # запрос на проигрывание звука
        return 0 # возвращаем ид занятого голоса, чтобы знать кого прекращать.
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
    def play(self, node):

        # получаем ноты и "вставляем" в генераторы

        # FIXME:
        # notes = node.compose()
        # for i in range(len(notes)):
        #     note, noteLen = notes[i]


        waveData1 = [
            self.waveGen.toBytes(0, 1),
            self.waveGen.toBytes(4, 2),
            self.waveGen.toBytes(7, 2),
            self.waveGen.toBytes(11, 1),
            self.waveGen.toBytes(14, 2),
            self.waveGen.toBytes(18, 2),
        ]

        waveData2 = [
            self.waveGen.toBytes(1, 1),
            self.waveGen.toBytes(5, 2),
            self.waveGen.toBytes(8, 2),
            self.waveGen.toBytes(12, 1),
            self.waveGen.toBytes(15, 2),
            self.waveGen.toBytes(19, 2),
        ]

        for i in range(len(self.voices)):
            self.voices[i].setData(waveData1[i])

        self.stopped = False

        for voice in self.voices:
            voice.start(self.p, self.bitrate)


        # Принцип проигрывания - как в SM, но не совсем
        # - для текущего таймкода курсора запрашиваем у всех текстов ноты
        # - если есть - отправляем в потоки
        # TODO: пул голосов
        # Голоса должны быть отдельно от инструментов. Они просо буферы
        # между потоками PortAudio и звукогенераторами
        # - переходим на следующий шаг тика
        # - sleep() согласно текущему темпу
        # TODO: обработка "управляющих" символов
        # Поскольку сетку долей будем полагать основой для композиции,
        # она будет общая для всех текстов - никаких нескольких дорожек
        # каждая со своим темпом. Как и в SM управляющие символы можно собрать
        # в единую дорожку.
        # Хороший вопрос - как в рамках одной дорожки совмещать ноты
        # бесконечной длины (как в SM) и конечной, как отслеживать,
        # для какой дорожки нота сменяется и тд

        cursor = Timecode(0, 0)
        while not self.stopped:
            # - для текущего таймкода курсора запрашиваем у всех текстов ноты
            currentNotes = []
            i = 0
            for text in texts:
                currentNotes[i] = text.getNotesAt(cursor)
                i += 1
                # с каждым текстом связать свой собственный микропул голосов

            # - если есть - отправляем в потоки

            # - переходим на следующий шаг тика
            # - sleep() согласно текущему темпу
            # TODO: обработка "управляющих" символов

        for i in range(3):
            print("sleep", i)
            time.sleep(1)

        for i in range(len(self.voices)):
            self.voices[i].setData(waveData2[i])

        for i in range(3):
            print("sleep", i)
            time.sleep(1)

        # terminate streams
        for voice in self.voices:
            voice.stop()

        # FIXME: call in destructor
        self.p.terminate()

        self.stopped = True
