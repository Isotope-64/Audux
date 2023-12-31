#       Importing modules. Most of these modules are simply here for sadtey, and make many python tasks easier
import os
import math
import numpy
import pygame
import nltk
from nltk.corpus import stopwords
#from nltk.stem import PorterStemmer     I have to do more research into stemming, this sub-library doesn't work right
stop_words = set(stopwords.words("english"))
#stemmer = PorterStemmer()
import matplotlib

#nltk.download('averaged_perceptron_tagger')
#nltk.download("stopwords")
#               ^^^^^^^^^^ This is the list of "stop words", which are words to be filtered out
#  It is most likely worth creating out own list of stop words, as there are many words that this list filters out, that we will not
#  want to, e.g "not"
#  Uncomment these dowload lines the first time this script is run on your device, then re-comment them

#  The quote chosen to test tokenizing
test_quote = "The crew of the USS Discovery discovered many discoveries. Discovering is what explorers do."

q_words = nltk.tokenize.word_tokenize(test_quote)
#  ^^^^ converts the words into a list of "tokens"
filtered_list = [word for word in q_words if word.casefold() not in stop_words]
#  ^^^^ checks each casefolded word, and adds to the new list if it's not in the list of stop words
tagged_list = nltk.pos_tag(q_words)
#  ^^^^ tags each of the words with their part of speech

#---Test prints:---
print("Filtered list  : ", filtered_list, "\n")
print("Tagged list    : ", tagged_list, "\n")

while (cmd := input("::> ")) != "":
    # loops infintely, assigning cmd to the user input. If the user inputs nothing, the loop breaks
    pass





