from Models.Word import Word
from Models.SearchChar import SearchChar
from Models.Direction import Direction 
from random import random 

# Manages all word search related functionality 
# This includes creating the word search and keeping track of found words / words left 
class SearchManager:
    wordsLeft = 0
    grid = [] 

    def __init__(self, listOfWords)
        self.listOfWords = listOfWords

    def start:
        print("Enter your words seperated by a comma.") 
        #take in users words
        words_str = input("Enter search words: ") 
        words_strs = words_str.split(",")
        words = []
        passes_validation =  True
        logest_word_length = 0

        for word in words_strs:

            if len(word) > 20:
                passes_validation = False
                break

            if len(word) > longest_word_length:
                longest_word_length = len(word) 

            if not word.isalpha():
                passes_validation = False
                break

            w = Word(word, 0, 0)
            words.append(w)

        if passes_validation:
            #display created word search 
            if longest_word_length < 10:
                longest_word_length = 10

            search_dimensions =  random.randint(longest_word_length, longest_word_length + 5)
            grid = Grid(search_dimensions) 
            for w in words:
                grid.insert_word(w)
        else:
            #didn't pass validation
            print("Words length can't be more than 20 characters long and word must contain only letters from the Alphabet.")

        

            



    


    #steps to create word search
    # 1. set grid w * h using logest word length 
    # 2.  
