from WordRetriever import get_words

words = []
ineligible_characters = []
guessed_words = []


def get_remaining_characters():
    return "".join(words)


def get_character_counts():
    character_string = get_remaining_characters()
    count_dictionary = {}
    for character in sorted(set(character_string)):
        character_count = character_string.count(character)
        count_dictionary[character] = character_count
    return count_dictionary


def get_word_scores():
    word_scores = {}
    character_counts = get_character_counts()
    for word in words:
        word_score = 0
        for character in set(word):
            # maybe remove the set?
            word_score += character_counts[character]
        word_scores[word] = word_score

    return word_scores


def get_next_word():
    word_scores = get_word_scores()
    next_word = min(word_scores, key=lambda x: word_scores[x])
    guessed_words.append(next_word)
    return next_word


def word_contains_ineligible_character(word):
    for character in word:
        if character in guess:
            return True
    return False


def get_eligible_words():
    eligible_words = []
    for character in guess:
        ineligible_characters.append(character)
    for word in words:
        if not word_contains_ineligible_character(word):
            eligible_words.append(word)
    return eligible_words


def print_output():
    print('Guesses are {0}\n'.format(', '.join(guessed_words)))
    print('Number of eligible words: {0}\n'.format(len(words)))
    print('Ineligible characters: {0}\n'.format(ineligible_characters))


if __name__ == '__main__':
    words = get_words()

    guess = get_next_word()
    words = get_eligible_words()
    print_output()
    guess = get_next_word()
    words = get_eligible_words()
    print_output()
    guess = get_next_word()
    words = get_eligible_words()
    print_output()
    guess = get_next_word()
    words = get_eligible_words()
    print_output()

