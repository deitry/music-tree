""" Принимает на вход ноду, раскрывает её и проигрывает содержимое """

import time
from datetime import datetime
import pyaudio as pa

# TODO: configure instruments/__init__.py
from music_tree.instruments.sin_wave import SinWave
from music_tree.base.timecode import Timecode, MAX_TICK
from music_tree.voice import Voice
from music_tree.sound_pool import MAX_VOICES

DEFAULT_BITRATE = 44100
TIME_DEBUG = False


class Player():
    def __init__(self, **kwargs):
        self._testMode = kwargs["test"] if "test" in kwargs else True
        # FIXME: вместо testMode сделать отдельный MockPlayer
        self.stopped = True
        self.last = datetime.now()

        self.bitrate = DEFAULT_BITRATE
        self.p = pa.PyAudio()
        self.stream = None

        # TODO:
        self.waveGen = SinWave(self.bitrate)
        # self.instruments = { "sin": SinWave(self.bitrate) }
        self.voices = []

        cnt = MAX_VOICES
        for _ in range(cnt):
            self.voices.append(Voice())

    # NOTE: blockable, but works through non-blockable callback
    def play(self, composition):  # node

        # получаем ноты и "вставляем" в генераторы
        text = composition.texts[0]

        self.stopped = False

        cursor = Timecode(0, 0)
        tempo = 120.
        # TODO: динамический расчёт задержки в зависимости от контекста
        delay = 60. / tempo / MAX_TICK

        VOICE_CNT = len(self.voices)

        if not self._testMode:
            REST = self.waveGen.rest()

        activeVoices = 0

        # Заблаговременно находим крайний элемент - когда останавливаться
        lastTimeCode = sorted(list(text.notes.keys()))[-1]
        if TIME_DEBUG: print("END AT:", lastTimeCode)

        # Запускаем голоса
        # TODO: В дальнейшем имеет смысл держать по пулу на каждый текст
        # TODO: запускать голоса имеет смысл, когда они на самом деле будут
        # использоваться. До этого можно держать их выключенными

        if not self._testMode:
            for voice in self.voices:
                voice.start(self.p, self.bitrate)

        prev = time.localtime()

        while not self.stopped:
            # - для текущего таймкода курсора запрашиваем у всех текстов ноты
            currentNotes = []

            # TODO: обработка "управляющих" символов

            # for text in texts:
            if cursor in text.notes:
                for note in text.notes[cursor]:
                    currentNotes.append(note)

            CUR_CNT = len(currentNotes)

            if CUR_CNT > 0 and not self._testMode:
                # - если есть - отправляем в потоки
                # Если нот нет, полагаем, что ничего делать не надо
                # TODO: начало пауз будет самостоятельным объектом
                # TODO: с каждым текстом связать свой собственный микропул голосов
                for i in range(CUR_CNT):
                    if i >= VOICE_CNT:
                        break

                    if TIME_DEBUG: print("before:", time.ctime())
                    waveData = self.waveGen.toBytes(currentNotes[i])
                    if TIME_DEBUG: print("middle:", time.ctime())
                    self.voices[i].setData(waveData)
                    if TIME_DEBUG: print("after:", time.ctime())

                # если в прошлый цикл активных голосов было больше, надо их занулить
                if CUR_CNT < activeVoices:
                    for i in range(activeVoices - CUR_CNT):
                        self.voices[CUR_CNT + i].setData(REST)

                        # TODO: стопить потоки неактивных голосов

                activeVoices = min(CUR_CNT, MAX_VOICES)

            # - sleep() согласно текущему темпу
            if not self._testMode:
                if TIME_DEBUG:
                    new = time.localtime()
                    print(delay, cursor, time.asctime(new), new.tm_sec - prev.tm_sec)
                    prev = new

                # в тестовом режиме не выдерживаем никаких пауз
                time.sleep(delay)

            # - переходим на следующий шаг тика
            cursor.incTick()

            # если достигли крайнего элемента - выходим
            if cursor >= lastTimeCode:
                self.stopped = True

        # terminate streams
        if not self._testMode:
            for voice in self.voices:
                voice.stop()

        # FIXME: call in destructor
        if not self._testMode: self.p.terminate()
