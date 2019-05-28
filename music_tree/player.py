""" Принимает на вход ноду, раскрывает её и проигрывает содержимое """

import time
from datetime import datetime
import pyaudio as pa

# TODO: configure instruments/__init__.py
from music_tree.instruments.sin_wave import SinWave

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


class Player():

    def __init__(self, **kwargs):
        self._testMode = kwargs["test"] if "test" in kwargs else True
        self.stopped = True
        self.last = datetime.now()

        self.bitrate = 44100
        self.p = pa.PyAudio()
        self.stream = None

        # TODO:
        self.waveGen = SinWave(self.bitrate)
        # self.instruments = { "sin": SinWave(self.bitrate) }
        self.voices = []

        for _ in range(3):
            self.voices.append(Voice())

    # NOTE: blockable, but works through non-blockable callback
    def play(self, node):

        # получаем ноты и "вставляем" в генераторы
        notes = node.getNotes()

        # FIXME:
        # for i in range(len(notes)):
        #     note, noteLen = notes[i]


        waveData = [
            self.waveGen.toBytes(0, 1),
            self.waveGen.toBytes(7, 2),
            self.waveGen.toBytes(10, 1),
        ]
        for i in range(3):
            self.voices[i].setData(waveData[i])

        self.stopped = False

        for voice in self.voices:
            voice.start(self.p, self.bitrate)

        for i in range(3):
            print("sleep", i)
            time.sleep(1)

        # terminate streams
        for voice in self.voices:
            voice.stop()

        # FIXME: call in destructor
        self.p.terminate()

        self.stopped = True
