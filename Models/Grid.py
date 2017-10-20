from random import random, randint, choice
import string
from copy import deepcopy
from .Direction import * 
from .SearchChar import *
from .GridPoint import * 

class Grid:
    cur_direction = Direction.HORIZONTAL
    dimension = 0
    max = 0

    def __init__(self, _dimension):
        self.dimension = _dimension 
        self.create_grid_points()

    def fill_in_blanks(self):
        for x in range(self.max):
            for y in range(self.max):
                if(self.grid_points[x][y] == ''):
                    self.grid_points[x][y] = choice(string.ascii_lowercase)


    def create_grid_points(self):
       self.max = self.dimension - 1 
       self.grid_points = [['']*self.dimension for i in range(self.dimension)]

       print("Dimension is {0} and Max is {1} and length of Matrix is {2}".format(self.dimension, self.max, len(self.grid_points)))
    
    def move_current_position(self, cur_x, cur_y):
        if self.cur_direction == Direction.HORIZONTAL:
            cur_x = cur_x + 1
        elif self.cur_direction == Direction.VERTICAL:
            cur_y = cur_y + 1
        elif self.cur_direction == Direction.UP_LEFT_DIAGNOL:
            cur_x = cur_x - 1
            cur_y = cur_y - 1
        elif self.cur_direction == Direction.UP_RIGHT_DIAGNOL:
            cur_x = cur_x + 1
            cur_y = cur_y - 1
        elif self.cur_direction == Direction.DOWN_LEFT_DIAGNOL:
            cur_x = cur_x - 1
            cur_y = cur_y + 1
        elif self.cur_direction == Direction.DOWN_RIGHT_DIAGNOL:
            cur_x = cur_x + 1
            cur_y = cur_y + 1
        return GridPoint(cur_x, cur_y)

    def check_length(self, word, x, y):
        if x > self.max - len(word) + 1 or y > self.max - len(word) + 1:
            return False
        return True

    def check_collision(self, word, cur_x, cur_y, direction):
        x = deepcopy(cur_x)
        y = deepcopy(cur_y)
        for c in word:
            if self.grid_points[x][y] == '' or self.grid_points[x][y] == c:
                grid_point = self.move_current_position(x, y)
                x = grid_point.x
                y = grid_point.y
            else:
                return False
        return True

    def insert_word(self, word):
        isValid = False
        cur_x = 0
        cur_y = 0
        directions = [Direction.HORIZONTAL, Direction.VERTICAL, Direction.UP_LEFT_DIAGNOL, Direction.UP_RIGHT_DIAGNOL, Direction.DOWN_LEFT_DIAGNOL, Direction.DOWN_RIGHT_DIAGNOL] 
        while not isValid:
            cur_x = randint(0, self.max - len(word) + 1)
            cur_y = randint(0, self.max - len(word) + 1) 
            self.cur_direction = choice(directions)
            x = deepcopy(cur_x)
            y = deepcopy(cur_y)
            isValid = self.check_collision(word, x, y, self.cur_direction) 

        for c in word:
            self.grid_points[cur_x][cur_y] = c
            grid_point = self.move_current_position(cur_x, cur_y)
            cur_x = grid_point.x
            cur_y = grid_point.y
