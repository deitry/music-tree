from music_tree.base.node import Node

class NoteNode(Node):
    
    def __init__(self):
        self.value = 0

    def play(self):
        print(self.value)
