import csv


def exclude_words_with_duplicate_letters(words):
    words_with_unique_characters = []
    for word in words:
        if len(set(word)) == len(word):
            words_with_unique_characters.append(word)
    return words_with_unique_characters


def count_vowels(string):
    num_vowels=0
    for char in string:
        if char in "AEIOU":
           num_vowels = num_vowels+1
    return num_vowels



def exclude_words_with_multiple_vowels(words):
    words_with_one_vowel = []
    for word in words:
        vowel_count = count_vowels(word)
        if vowel_count == 1:
            words_with_one_vowel.append(word)
    return words_with_one_vowel



def get_words():
    five_letter_words = []
    with open('words.txt', 'r') as fd:
        reader = csv.reader(fd)
        for row in reader:
            five_letter_words.append(row[0].upper())
    words_with_unique_letters = exclude_words_with_duplicate_letters(five_letter_words)
    words_with_a_single_vowel = exclude_words_with_multiple_vowels(words_with_unique_letters)
    return words_with_a_single_vowel

