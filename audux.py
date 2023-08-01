#       Importing modules. Most of these modules are simply here for safety, and make many python tasks easier
import os
import math
import numpy
import pygame
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import nltk
from nltk.stem import WordNetLemmatizer
l = WordNetLemmatizer()
import audux_commands as ac

class Word():
    def __init__(self, string):
        tagged_word = nltk.pos_tag([string])[0]
        self.val = l.lemmatize(string)#, tagged_word[1])
        self.type = tagged_word[1]

while (cmd := input("<:: ")) != "":
    # loops infintely, assigning cmd to the user input. If the user inputs nothing, the loop breaks
    words = nltk.tokenize.word_tokenize(cmd)
    words = [Word(w) for w in words] # word
    ac.interpret_command(words[0], words[1:])





