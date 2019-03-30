from music_tree.base.composition import Timecode
import os

class Marker():

    def __init__(self, timecode, name):
        self.timecode = timecode
        self.name = name

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Marker):
            return self.timecode == other.timecode and self.name == other.name
        return False


class MarkerWorker():

    def __init__(self, fileName="markers"):
        self.fileName = fileName

    def addMarker(self, marker):
        # print to file
        with open(self.fileName,'w') as f:
            # FIXME: запись в соответствующее место, чтобы маркеры шли по порядку
            # TODO: проверка на то, что в данном месте маркер уже есть?
            f.write('%s %s %s' % (marker.timecode.beat, marker.timecode.tick, marker.name))

    def getMarkers(self):
        # read all markers from file

        markers = []

        with open(self.fileName,'r') as f:
            for line in f:
                words = line.split()
                timecode = Timecode(words[0], words[1])
                markers.append(Marker(timecode, words[2]))

        return markers
