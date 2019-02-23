""" Принимает на вход ноду, раскрывает её и проигрывает содержимое """

import math
from pyaudio import PyAudio
from datetime import datetime, timedelta


class Player():
    def __init__(self):
        self.stopped = True
        self.last = datetime.now()

        self.bitrate = 16000
        self.p = PyAudio()
        self.stream = None

    def play(self, node):

        raise NotImplementedError # FIXME

        # TODO: на основе содержимого нод определяем список нужных инструментов
        instruments = node.getInstruments()

        # TODO: раскрывать ноды в единую ленту?

        pos = 0

        while not self.stopped:
            pos += 1
            for instrument in instruments:
                # TODO: кто кого и как должен вызывать?
                # notes = node.getNotes(instrument)
                # instrument.play(notes)
                notes = instrument.getNotes(node, pos)
                instrument.play(notes)

    def testPlay(self, note, noteLen):

        if self.stream == None:
            raise AssertionError("Must be called in context manager")

        noteHz = 440 * pow(2., note / 12.)

        FREQUENCY = noteHz
        LENGTH = noteLen

        NUMBEROFFRAMES = int(self.bitrate * LENGTH)

        WAVEDATA = ''

        MAX = 128 # по сути отвечает за громкость
        MAX_2 = int(MAX / 2)

        CENTER = MAX_2

        for x in range(NUMBEROFFRAMES):
            WAVEDATA += chr(
                int(
                    math.sin(x / ((self.bitrate / FREQUENCY) / math.pi)) *
                    (MAX_2 - 1) + CENTER))

        time = datetime.now()
        delta = timedelta(seconds=noteLen)

        # для отладки задержек
        # print("times: ", time, self.last, delta)
        # len(WAVEDATA) / BITRATE,
        # print("len: ",  time - self.last - delta)

        self.last = time
        self.stream.write(WAVEDATA)

    def __enter__(self):
        self.stream = self.p.open(
            format=self.p.get_format_from_width(1),
            channels=1,
            rate=self.bitrate,
            output=True)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()
