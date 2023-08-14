#       Importing modules. Most of these modules are simply here for safety, and make many python tasks easier
from os import environ, walk
from importlib import import_module
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from nltk import RegexpParser, tokenize, pos_tag, stem as _l
l = _l.WordNetLemmatizer()
c = RegexpParser("NP: {<DT>?<JJ>*<NN>}")

files = []
for (dir_path, dir_names, file_names) in walk("__commands"): files.extend([f[:-3] for f in file_names if f[-3:] == ".py"])

#       Making a class for each word. When the word is initialised, it automatically gets processed.
#This allows for in future creating functions that affect the words
class Word():
    def __init__(self, string, type):
        self.original_text = string # --> just in case we ever need to access this
        self.val = l.lemmatize(string) # --> the root of the word. This is typically the useful bit. E.g cases->case worst->bad
        self.type = type # --> the part of speech. E.g adjective, noun
    def __str__(self) -> str: return str(self.val)

def interpret_command(cmd : Word, args : list = []):
    if cmd.val in files:
        command_file = import_module("__commands." + cmd.val)
        command_file.fnc(args)

while (cmd := input("<:: ")) != "":
    # loops infintely, assigning cmd to the user input. If the user inputs nothing, the loop breaks
    words = tokenize.word_tokenize(cmd) # --> separates the string into words
    words = pos_tag(words)
    words = c.parse(words)
    interpret_command(Word(*words[0][0]))


