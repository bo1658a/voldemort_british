import sys
from itertools import permutations
from collections import Counter
import load_dictionary

def main():
    """Load files, run filters, allow user to view anagrams by 1st letter."""
    name = 'tmvoordle'
    name = name.lower()

    word_list_ini = load_dictionary.load('2of4brif.txt')
    trigrams_filtered = load_dictionary.load('least-likely_trigrams.txt')

    word_list = prep_words(name, word_list_ini)
    filtered_cv_map = cv_map_words(word_list)
    filtered_1 = cv_map_filter(name, filtered_cv_map)
    filtered_2 = trigram_filter(filter_1, trigrams_filtered)
    filtered_3 = letter_pair_filter(filter_2)
    view_by_letter(name, filter_3)
