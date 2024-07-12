#
# Zachary Deinhammer
# 07/12/2024
# Test class to store a Scrabble dictionary and search if a given word
# is contained within that dictionary
#

class ScrabbleSearch(object):
    # Constructor - takes the file specified in the main function
    # and stores words into an alphabetical dictionary
    def __init__(self, file):
        self.sorted_words = {'A': [], 'B': [], 'C': [],
                             'D': [], 'E': [], 'F': [],
                             'G': [], 'H': [], 'I': [],
                             'J': [], 'K': [], 'L': [],
                             'M': [], 'N': [], 'O': [],
                             'P': [], 'Q': [], 'R': [],
                             'S': [], 'T': [], 'U': [],
                             'V': [], 'W': [], 'X': [],
                             'Y': [], 'Z': []}

        # Stores words in list to be sorted by self.sorted_words later
        words = []
        for line in file:
            line = list(line.strip('\n'))
            words.append(line)
        # Removes the title and first blank line of file
        words.pop(0)
        words.pop(0)

        # Iterates through words and then stores each words in
        # the proper place in self.sorted_words
        for idx in range(len(words)):
            first_letter = words[idx][0]
            for l in self.sorted_words:
                if first_letter == l:
                    self.sorted_words[l].append(words[idx])

    # Returns length of provided letter category
    def __len__(self, letter):
        letter = letter.upper()
        return len(self.sorted_words[letter])

    # Takes a user provided word and searches to see if
    # user provided word is in the scrabble dictionary, returning True if
    # found and False otherwise
    def binary_search(self, user_word):
        user_word = list(user_word.upper())
        list_to_search = self.sorted_words[user_word[0]]

        l = 0
        r = len(list_to_search) - 1

        while l <= r:
            mid = (l + r) // 2
            if list_to_search[mid] == user_word:
                return True

            if list_to_search[mid] < user_word:
                l = mid + 1
            else:
                r = mid - 1

        return False


def main():

    with open('Collins Scrabble Words (2019).txt', 'r') as file:
        search1 = ScrabbleSearch(file)

    selection = ''
    while selection != 'N':
        user_word = input('Enter a word to search for: ')
        result = search1.binary_search(user_word)
        if result:
            print(f'{user_word} is in the dictionary.')
        else:
            print(f'{user_word} is not in the dictionary.')
        selection = input('Do you wish to search again? (Y/N): ').upper()

    print('Finished.')


main()



