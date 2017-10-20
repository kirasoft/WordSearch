from Models.Word import Word
from Models.SearchChar import SearchChar
from Models.Direction import Direction 
from Models.Grid import Grid
from random import randint

# Manages all word search related functionality 
# This includes creating the word search and keeping track of found words / words left 
class SearchManager:
    words_left = 0
    grid = [] 
    word_list = [] 

    def start():
        print("Enter your words seperated by a comma.") 
        #take in users words
        words_str = input("Enter search words: ") 
        words_strs = words_str.split(",")
        passes_validation =  True
        longest_word_length = 0

        for word in words_strs:

            if len(word) > 20:
                passes_validation = False
                break

            if len(word) > longest_word_length:
                longest_word_length = len(word) 

            if not word.isalpha():
                passes_validation = False
                break

        if passes_validation:
            #display created word search 
            if longest_word_length < 10:
                longest_word_length = 10

            search_dimensions = randint(longest_word_length, longest_word_length + 5)
            grid = Grid(search_dimensions) 
            for w in words_strs:
                grid.insert_word(w)
            grid.fill_in_blanks()
            with open('wordsearch.txt','w') as f:
                for x in range(grid.max):
                    for y in range(grid.max): 
                        f.write(grid.grid_points[x][y])
                    f.write('\n')
        else:
            #didn't pass validation
            print("Words length can't be more than 20 characters long and word must contain only letters from the Alphabet.")
