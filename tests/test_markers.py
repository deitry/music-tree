from music_tree.marker_worker import MarkerWorker, Marker
from music_tree.base.composition import Timecode

def test_00_setup():
    assert 0 == 0

def test_01_readFromFile():
    worker = MarkerWorker(fileName='resources\\markers_example')
    markers = worker.getMarkers()
    assert len(markers) == 4

def test_02_writeToFile():
    worker = MarkerWorker(fileName='resources\\markers_write_test')
    marker = Marker(Timecode(4, 30), "test1")
    worker.addMarker(marker)
    markers = worker.getMarkers()
    assert markers[-1] == marker and len(markers) == 1
