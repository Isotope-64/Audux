#       Importing modules. Most of these modules are simply here for safety, and make many python tasks easier
import os
import math #unused. Most likely will not be in this file, but it's better to be safe than sorry.
import numpy #unused. Again, is similar to the math module, just more advanced
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame #unused. Will be used whenever we need to render anything to the inbuilt screen
import nltk
from nltk.stem import WordNetLemmatizer
l = WordNetLemmatizer()
import audux_commands as ac

#       Making a class for each word. When the word is initialised, it automatically gets processed.
#This allows for in future creating functions that affect the words
class Word():
    def __init__(self, string):
        self.original_text = string # --> just in case we ever need to access this
        #to tag the word, we need to put it into a list. 
        tagged_word = nltk.pos_tag([string])[0]
        #We then need to access from the list^
        self.val = l.lemmatize(string) # --> the root of the word. This is typically the useful bit. E.g cases->case worst->bad
        self.type = tagged_word[1] # --> the part of speech. E.g adjective, noun

while (cmd := input("<:: ")) != "":
    # loops infintely, assigning cmd to the user input. If the user inputs nothing, the loop breaks
    words = nltk.tokenize.word_tokenize(cmd) # --> separates the string into words
    words = [Word(w) for w in words] # word
    #creates a Word object for each word, and replaces the text object in the list with that object
    ac.interpret_command(words[0], words[1:]) # --> the function to interpret the commands. The first word of the command is
    #                                               always the command itself, and the following words are arguments





