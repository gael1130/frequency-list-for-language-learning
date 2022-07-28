# functions defined to sort the frequency of words in a text


def remove_selected_elements(list_of_words, stopwords):
    """
    Given a list of words (list_of_words), remove a list of selected words (stopwords) from it
    :param list_of_words: list of words
    :param stopwords: list of words to remove from original list
    :return:
    """
    return [w for w in list_of_words if w not in stopwords]


def word_list_to_freq_dict(list_of_words):
    """
    Given a list of words, return a dictionary of word-frequency pairs
    :param list_of_words: a list of words
    :return: a dictionary of word-frequency pairs
    """
    wordfreq = [list_of_words.count(p) for p in list_of_words]
    return dict(list(zip(list_of_words, wordfreq)))


def sort_freq_dict(freq_dictionary):
    """
    Sort a dictionary of word-frequency pairs in order of descending frequency
    :param freq_dictionary: a dictionary of frequencies of word as keys, word as value
    :return: a list of tuples (frequency, word)
    """
    aux = [(freq_dictionary[key], key) for key in freq_dictionary]
    aux.sort()
    aux.reverse()
    return aux

# thanks to:
# https://programminghistorian.org/en/lessons/counting-frequencies

# gives other libraries to try
# https://towardsdatascience.com/how-to-extract-text-from-pdf-245482a96de7

# check this too
# https://lexiteria.com/word_frequency/finnish_word_frequency_list.html
