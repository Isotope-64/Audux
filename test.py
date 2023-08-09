import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
stop_words = set(stopwords.words("english")) # <-- this is a bad list of words
l = WordNetLemmatizer()

def fnc(args):
    test_quote = "The friends of DeSoto love scarves." if len(args) <= 0 else "".join([i.val + " " for i in args])
    #  ^^^^ the quote chosen to test tokenizing
    q_words = nltk.tokenize.word_tokenize(test_quote)
    #  ^^^^ converts the words into a list of "tokens"
    filtered_list = [word for word in q_words if word.casefold() not in stop_words]
    #  ^^^^ checks each casefolded word, and adds to the new list if it's not in the list of stop words
    tagged_list = nltk.pos_tag(q_words)
    #  ^^^^ tags each of the words with their part of speech
    lemmatized_list = [l.lemmatize(word) for word in q_words]
    #  ^^^^ converts each of the words to their lemmas

    #---Test Prints---
    print("Test quote     : ", test_quote, "\n")
    print("Filtered list  : ", filtered_list, "\n")
    print("Tagged list    : ", tagged_list, "\n")
    print("Lemmatized list: ", lemmatized_list, "\n")