""" Принимает на вход ноду, раскрывает её и проигрывает содержимое """

from pyaudio import PyAudio
from datetime import datetime, timedelta

from music_tree.instruments.sin_wave import SinWave

class Player():
    def __init__(self, **kwargs):
        self._testMode = kwargs["test"] if "test" in kwargs else True
        self.stopped = True
        self.last = datetime.now()

        self.bitrate = 16000
        self.p = PyAudio()
        self.stream = None

        # TODO:
        # self.instruments
        self.sinWave = SinWave(self.bitrate)

    def play(self, node):

        notes = node.getNotes()
        # TODO: ноты как объекты с положением
        for note, noteLen in notes:
            self.testPlay(note, noteLen)

        # TODO: на основе содержимого нод определяем список нужных инструментов
        # instruments = node.getInstruments()

        # TODO: раскрывать ноды в единую ленту?

        # while not self.stopped:
        #     pos += 1
        #     for instrument in instruments:
        #         # TODO: кто кого и как должен вызывать?
        #         # notes = node.getNotes(instrument)
        #         # instrument.play(notes)
        #         notes = instrument.getNotes(node, pos)
        #         instrument.play(notes)

    # TODO: rename to playNote
    # FIXME: must be non-blockable
    def testPlay(self, note, noteLen):

        if self.stream == None:
            raise AssertionError("Must be called in context manager")

        waveData = self.sinWave.toBytes(note, noteLen)

        # time = datetime.now()
        # delta = timedelta(seconds=noteLen)

        # для отладки задержек
        # print("times: ", time, self.last, delta)
        # len(WAVEDATA) / BITRATE,
        # print("len: ",  time - self.last - delta)

        # self.last = time

        # TODO: итеративная запись в поток - порциями получать и писать байты
        # TODO: несколько нот одновременно?
        if not self._testMode:
            print("stream.write")
            self.stream.write(waveData)

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
