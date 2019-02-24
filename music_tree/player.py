""" Принимает на вход ноду, раскрывает её и проигрывает содержимое """

from pyaudio import PyAudio
from datetime import datetime, timedelta

# TODO: configure instruments/__init__.py
from music_tree.instruments.sin_wave import SinWave
from music_tree.instruments.triangle_wave import TriangleWave
from music_tree.instruments.square_wave import SquareWave


# TODO: move to class or lambda
def callback(in_data, frame_count, time_info, status):
    data = wf.readframes(frame_count)
    return (data, pyaudio.paContinue)


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
        self.waveGen = SinWave(self.bitrate)
        self.gens = []
        self.gens[0] = SinWave(self.bitrate)
        self.gens[1] = SinWave(self.bitrate)
        self.gens[2] = SinWave(self.bitrate)

    # NOTE: blockable, but works through non-blockable callback
    def play(self, node):

        # start streams
        # TODO: callback as lambda

        for i in range(3):
            self.streamPool[i] = self.p.open(
                format=self.p.get_format_from_width(1),
                channels=1,
                rate=self.bitrate,
                output=True,
                stream_callback=lambda in_data, frame_count, time_info, status: print(frame_count)
            )

            self.streamPool[i].start_stream()


        notes = node.getNotes()
        for i in range(len(notes)):
            note, noteLen = notes[i]
            self.gens[i].makeWave(note, noteLen)

        # TODO: ноты как объекты с положением
        #for note, noteLen in notes:
            #self.testPlay(note, noteLen)

        # terminate streams


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
    # NOTE: blockable
    def testPlay(self, note, noteLen):

        if self.stream == None:
            raise AssertionError("Must be called in context manager")

        waveData = self.waveGen.toBytes(note, noteLen)

        # time = datetime.now()
        # delta = timedelta(seconds=noteLen)

        # для отладки задержек
        # print("times: ", time, self.last, delta)
        # len(WAVEDATA) / BITRATE,
        # print("len: ",  time - self.last - delta)

        # self.last = time

        # TODO: итеративная запись в поток - порциями получать и писать байты
        # TODO: несколько нот одновременно?
        # https://people.csail.mit.edu/hubert/pyaudio/docs/
        if not self._testMode:
            print("stream.write")
            self.stream.write(waveData)

    def __enter__(self):
        self.stream = self.p.open(
            format=self.p.get_format_from_width(1),
            channels=1,
            rate=self.bitrate,
            output=True,
            stream_callback=callback)

        self.stream.start_stream()

        # TODO: ?
        # while stream.is_active():
        #     time.sleep(0.1)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

