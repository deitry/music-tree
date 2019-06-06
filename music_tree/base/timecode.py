MAX_TICK = 32


class Timecode():
    def __init__(self, beat, tick):

        self.beat = max([beat, 0])
        self.tick = min([max([tick, 0]), MAX_TICK])

    def incTick(self):

        self.tick += 1
        if self.tick >= MAX_TICK:
            self.tick = 0
            self.beat += 1

    def dec(self):
        self.tick -= 1
        if self.tick < 0:
            self.tick = MAX_TICK - 1
            self.beat -= 1

    def __gt__(self, other):
        if isinstance(other, Timecode):
            return any([
                self.beat > other.beat, self.beat == other.beat
                and self.tick > other.tick
            ])
        return False

    def __ge__(self, other):
        if isinstance(other, Timecode):
            return any([
                self.beat > other.beat, self.beat == other.beat
                and self.tick >= other.tick
            ])
        return False

    def __lt__(self, other):
        if isinstance(other, Timecode):
            return any([
                self.beat < other.beat, self.beat == other.beat
                and self.tick < other.tick
            ])
        return False

    def __eq__(self, other):
        if isinstance(other, Timecode):
            return all([self.beat == other.beat, self.tick == other.tick])
        return False

    def __repr__(self):
        return str(self.beat) + ":" + str(self.tick)

    def __hash__(self):
        return hash((self.beat, self.tick))

    # TODO: операции сложения, вычитания и умножения
    # Умножение может пригодится для 3*QUARTER, где QUARTER==Timecode(1,0)
