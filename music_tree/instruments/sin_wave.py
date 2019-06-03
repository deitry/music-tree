""" Basic sin wave generator """

import math
import pyaudio


class SinWave():

    def __init__(self, bitrate):
        self.bitrate = bitrate

    def generate(self, how_many_bytes, freq, amplitude):
        # print("generate ", how_many_bytes, freq, amplitude)

        data = ''
        for i in range(how_many_bytes):
            data += chr(int(i % freq / freq * amplitude))

        return data

    def generateSingleWave(self, freq, amplitude):
        # print("generate 1w", freq, amplitude)

        data = ''
        # TODO: возвращать не байты, а генератор?
        samplesForFreq = self.bitrate / freq
        for i in range(samplesForFreq):
            arg = (i % samplesForFreq) / samplesForFreq
            val = math.sin(math.pi * arg)
            data += chr(int(val))

        # print("generate", len(data), data)
        return data

    def toBytes(self, note, noteLen=0):
        """ Returns bytes representation of given note """

        noteHz = 220 * pow(2., note / 12.)

        FREQUENCY = noteHz
        LENGTH = noteLen if noteLen > 0 else 1 / FREQUENCY

        NUMBEROFFRAMES = int(self.bitrate * LENGTH)

        WAVEDATA = ''

        MAX = 128 # по сути отвечает за громкость
        MAX_2 = int(MAX / 2)

        CENTER = MAX_2

        for x in range(NUMBEROFFRAMES):
            WAVEDATA += chr(
                int(
                    math.sin(x / ((self.bitrate / FREQUENCY) / math.pi)) *
                    (MAX_2 - 1) + CENTER
                )
            )

        return WAVEDATA

    def rest(self):
        """ Генерируем байты для паузы, чтобы не прерывать поток """

        data = ''
        for _ in range(24):
            data += chr(0)

        return data
