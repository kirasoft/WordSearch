from Direction import Direction 

class Word:

    #Direction the word reads (horizontal, vertical, diagnol) 
    def _get_direction(self):
        return self.__direction
    def _set_direction(self, value):
        if not isinstance(value, Direction):
            raise TypeError("direction must be set to a Direction Enum value")
        self.__direction = value
    direction = property(_get_direction, _set_direction)

    def __init__(self, word, x, y):
        self.word = word
        self.x = x
        self.y = y
        self.length = len(word) 
        self.direction = Direction.Horizontal  

