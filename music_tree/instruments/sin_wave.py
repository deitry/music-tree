""" Basic sin wave generator """

import math
import pyaudio


class SinWave():
    def __init__(self, bitrate):
        self.bitrate = bitrate

    def callback(self, in_data, frame_count, time_info, status):
        print("thats mee")

        # пока не работает генерация, создаём звук прямо здесь
        data = ''
        MAX = 10
        PERIOD = 100

        for i in range(frame_count):
            data += chr(int(i % PERIOD / PERIOD * MAX))

        # TODO:
        # data = self.yieldBytes(frame_count)

        flag = pyaudio.paContinue if len(data) > 0 else pyaudio.paComplete
        print(len(data), flag)

        return (data, flag)


    def toBytes(self, note, noteLen):
        """ Returns bytes representation of given note """

        noteHz = 440 * pow(2., note / 12.)

        FREQUENCY = noteHz
        LENGTH = noteLen

        NUMBEROFFRAMES = int(self.bitrate * LENGTH)

        WAVEDATA = ''

        MAX = 128  # по сути отвечает за громкость
        MAX_2 = int(MAX / 2)

        CENTER = MAX_2

        for x in range(NUMBEROFFRAMES):
            WAVEDATA += chr(
                int(
                    math.sin(x / ((self.bitrate / FREQUENCY) / math.pi)) *
                    (MAX_2 - 1) + CENTER))

        return WAVEDATA

    def makeWave(self, note, noteLen):
        self.wave = self.toBytes(note, noteLen)

    # сейчас использование ведёт к TypeError. TODO: научиться готовить генераторы
    def yieldBytes(self, n):
        print ("eee")
        cnt = 0
        data = bytes()

        for i in range(len(self.wave)):

            data += chr(int(self.wave[i]))
            cnt += 1
            if cnt >= n:
                res = data
                data = []
                yield res
