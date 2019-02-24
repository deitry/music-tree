""" Basic triangle wave generator """

import math

class TriangleWave():

    def __init__(self, bitrate):
        self.bitrate = bitrate

    def toBytes(self, note, noteLen):
        """ Returns bytes representation of given note """

        noteHz = 440 * pow(2., note / 12.)

        FREQUENCY = noteHz
        LENGTH = noteLen

        NUMBEROFFRAMES = int(self.bitrate * LENGTH)

        WAVEDATA = ''

        MAX = 64  # по сути отвечает за громкость
        MAX_2 = int(MAX / 2)

        CENTER = MAX_2

        PERIOD = self.bitrate / FREQUENCY

        # TODO: заранее вычислять базовый семпл? генератор?
        for x in range(NUMBEROFFRAMES):
            WAVEDATA += chr(
                int(
                    (x % PERIOD) / PERIOD * MAX
                )
            )


        return WAVEDATA
