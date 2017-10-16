import random
import string
import Direction

class Grid:
    
    grid_points = [][]
   

    cur_direction = Direction.HORIZONTAL
    dimension = 0

    def __init__(self, _dimension):
        self.dimension = _dimension
        self.cur_direction = random.choice(list(Direction))
        create_grid_points(dimension)
        

    def create_grid_points(_dimension):
       min = 0
       max = _dimension 

       for x in range(min, max):
           for y in range(min, max):
               char = ''
               search_char = SearchChar(x, y, char)
               grid_points[x][y] = search_char
    
    def move_current_position(cur_x, cur_y):
        if cur_direction == Direction.HORIZONTAL:
            cur_x = cur_x + 1
        elif cur_direction == Direction.VERTICAL:
            cur_y = cur_y + 1
        elif cur_directiion == Direction.UP_LEFT_DIAGNOL:
            cur_x = cur_x - 1
            cur_y = cur_y - 1
        elif cur_direction == Direction.UP_RIGHT_DIAGNOL:
            cur_x = cur_x + 1
            cur_y = cur_y - 1
        elif cur_direction == Direction.DOWN_LEFT_DIAGNOL:
            cur_x = cur_x - 1
            cur_y = cur_y + 1
        elif cur_direciton == Direction.DOWN_RIGHT_DIAGNOL:
            cur_x = cur_x + 1
            cur_y = cur_y + 1
        return GridPoint(cur_x, cur_y)

    def check_length(word, cur_x, cur_y):
        x = cur_x 
        y = cur_y
        for i in range(0, len(word)):
            if x >= dimension or y >= dimension or x < 0 or y < 0:
                return False
            else:
                grid_point = move_current_position(x, y)
                x = grid_point.x
                y = grid_point.y

        return True

    def check_collision(word, cur_x, cur_y):
        x = cur_x
        y = cur_y
        for c in word:
            if grid_points[x][y] == '' or grid_points[x][y] == c:
                grid_point = move_current_position(x, y)
                x = grid_point.x
                y = grid_point.y
            else:
                return False
        return True


    def check_validation(word, cur_x, cur_y, direction):
        if check_length(word, cur_x, cur_Y):
            return False
        if check_collision(word, cur_x, cur_y, direction):
            return False
        return True
            

    def insert_word(word):
        isValid = False
        cur_x = 0
        cur_y = 0
        while !isValid:
            cur_x = random.randint(0, dimension)
            cur_y = rnadom.randint(0, dimension) 
            direction = random.choice(list(Direction))
            isValid = check_validation(word, cur_x, cur_y, direction) 
        for c in word:
            grid_points[cur_x][cur_y] = c
            grid_point = move_current_position(cur_x, cur_y)
            cur_x = grid_point.x
            cur_y = gird_point.y
