from .Direction import * 

class Word:
    word = ""
    x = 0
    y = 0
    length = 0

    def __init__(self, word, x, y):
        self.word = str(word)
        self.x = x
        self.y = y
        self.length = len(word) 
        self.direction = Direction.HORIZONTAL  

