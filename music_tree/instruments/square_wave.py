""" Basic square wave generator """

import math

class SquareWave():

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
        PERIOD = self.bitrate / FREQUENCY
        PERIOD_2 = PERIOD / 2

        # TODO: заранее вычислять базовый семпл? генератор?
        for x in range(NUMBEROFFRAMES):
            WAVEDATA += chr(
                int(
                    MAX if x % PERIOD < PERIOD_2 else 0
                )
            )


        return WAVEDATA
