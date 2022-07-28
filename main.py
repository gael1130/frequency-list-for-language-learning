# importing required modules
from commands import *
from PyPDF2 import PdfReader
from itertools import islice
import pprint

# Get a pdf and extract the text from it
reader = PdfReader("data/book_exemple.pdf")
text = ""
for page in reader.pages:
    text += page.extract_text() + "\n"

# split text into words
wordlist = text.split()

# make the words lowercase
lowercase_list = [word.lower() for word in wordlist]

# remove punctuation, elements and words I want to exclude
elements_to_remove = ['—', "_", ".", "1", "~7a"]
list_without_punctuation = remove_selected_elements(lowercase_list, elements_to_remove)

# a list comprehension to count occurences
wordfreq = [list_without_punctuation.count(w) for w in list_without_punctuation]

# Create a dictionary of word-frequency pairs
frequency_dictionary = word_list_to_freq_dict(list_without_punctuation)
pp = pprint.PrettyPrinter(indent=4)

# sort the dictionary from most to least frequent
sorted_dictionary = sort_freq_dict(frequency_dictionary)

# filter the data to have a list of 99 elements ranked by frequency
filtered = (i for i in sorted_dictionary if i[0] >= 10)
top_99 = list(islice(filtered, 99))

# pp.pprint(top_99)
