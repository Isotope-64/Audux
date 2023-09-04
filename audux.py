#       Importing modules. Most of these modules are simply here for safety, and make many python tasks easier
from os import walk # --> for locating the files for the commands
from importlib import import_module # --> for loading the files as python modules
from nltk import RegexpParser, tokenize, pos_tag # --> for processing the strings
c = RegexpParser("NP: {<DT>?<JJ>*<NN>}") # --> for grouping the words and processing them better
import speech_recognition as sr # --> for converting audio into strings
r = sr.Recognizer() # --> a python object that takes in audio and outputs strings

run = True # --> ...is the code running or not... this is fairly simple

#       Making a list containing all of the python files. It walks through all of the files and subfolders within __commands, 
# and adds them to the list, minus the .py at the end
files = []
for (dir_path, dir_names, file_names) in walk("__commands"): files.extend([f[:-3] for f in file_names if f[-3:] == ".py"])

#       Making a class for each word. When the word is initialised, it assigns the value and type
#This allows for in future creating functions that affect the words
class Word():
    def __init__(self, string, type = -1):
        self.val = string # --> the word itself as a string
        self.type = type # --> the part of speech. E.g adjective, noun
    def __str__(self) -> str: return str(self.val)

#       Making a function that takes in word objects as the command name, and a list of word objecs as the arguments. Then looks through the list of python fils
# and chooses the appropriate one. It then imports that as a module and runs the function named fnc within it.
def interpret_command(cmd : Word, args : list = []):
    if cmd.val in files:
        command_file = import_module("__commands." + cmd.val)
        command_file.fnc(args)


while run:
    print("### Speak Command ###")
    with (mic := sr.Microphone()) as source: cmd = r.listen(source) # --> records the microphone input. Don't ask me how that works
    cmd = r.recognize_sphinx(cmd) # --> converts the audio into a string
    print("## " + cmd)
    del mic # --> delete the microphone
    
    # loops infintely, assigning cmd to the user input. If the user inputs nothing, the loop breaks
    words = pos_tag(tokenize.word_tokenize(cmd)) # --> separates the total string into individual words, then tags each one with a part of speech
    words_tree = c.parse(words) # --> chunks the words. separates it into groups such as "brown bag" or "ran fast"
    interpret_command(Word(*words[0]), [Word(*i) for i in words][1:]) # --> separates the first word of the sentence, 
    #                                                                      then the rest of the words, and applies the reviously made function


