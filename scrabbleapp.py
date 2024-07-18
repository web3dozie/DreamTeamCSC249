import re
from collections import Counter
from sortedcontainers import SortedSet


class ScrabbleApp:
    def __init__(self, filename='Collins Scrabble Words (2019).txt'):
        # Load the words from the dictionary file into the data structures.
        with open(filename, 'r') as file:
            word_list = [line.strip() for line in file][2:]

        self.words = SortedSet(word_list)  # Initialize the word list

    def add_word(self, word):
        if re.match('^[A-Z]+$', word):  # Only actual words can be added
            self.words.add(word.upper())  # Add word to the sorted set

    def remove_word(self, word):
        try:
            self.words.remove(word.upper())
        except KeyError:
            pass  # Word does not exist, allowing a silent error is more efficient than existence checks

    def is_valid_word(self, word):
        return word.upper() in self.words  # O(log n) sorted sets use binary search

    def find_words_from_letters(self, letters, wildcards=0):
        letters = letters.upper()
        letter_set = set(letters)
        letter_count = Counter(letters)

        valid_words = []

        # Use set intersection to reduce candidates
        candidates = [word for word in self.words if
                      set(word).issubset(letter_set) or len(set(word) - letter_set) <= wildcards]

        for word in candidates:
            if len(word) <= len(letters) + wildcards:
                word_count = Counter(word)

                # Counter comparison
                if all(max(count - letter_count.get(char, 0), 0) <= wildcards for char, count in word_count.items()):
                    valid_words.append(word)

        return valid_words

    def word_score(self, word):
        # Dictionary for scoring
        letter_points = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4,
                         'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1,
                         'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1,
                         'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8,
                         'Y': 4, 'Z': 10}

        word = word.upper()
        score = 0

        # Iterates through word to calculate total points
        if self.is_valid_word(word):
            for letter in word:
                score += letter_points[letter]

            # If word uses all tiles (7 or 8 if building off another word) 50 points are added to total
            if len(word) >= 7:
                score += 50

            return score
        else:
            pass
