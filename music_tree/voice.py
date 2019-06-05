import pyaudio as pa


class Voice():
    """ Принимает байты от звукогенератора и воспроизводит их.
        Один голос - одна нота - один поток. """

    def __init__(self):
        self._buffer = [chr(0)]  # соответственно частоте дискретизации
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
            stream_callback=self.callback)

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
        self.current = 0

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
