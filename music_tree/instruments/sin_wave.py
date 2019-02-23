""" Basic sin wave generator """

import math

class SinWave():

    def __init__(self, bitrate):
        self.bitrate = bitrate

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

        # TODO: заранее вычислять базовый семпл? генератор?
        for x in range(NUMBEROFFRAMES):
           WAVEDATA += chr(
               int(
                   math.sin(x / ((self.bitrate / FREQUENCY) / math.pi)) *
                   (MAX_2 - 1) + CENTER))


        return WAVEDATA
