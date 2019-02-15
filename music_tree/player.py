""" Принимает на вход ноду, раскрывает её и проигрывает содержимое """

class Player():

    def __init__(self):
        self.stopped = True

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
