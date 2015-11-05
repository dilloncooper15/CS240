import words


def main():
    """ Nonetype -> Nonetype
    The main logic of the program.
    """
    stats = []
    while True:
        game = play_round()
        stat = {'guesses': game[0], 'correct': game[1], 'word': game[2]}
        stats.append(stat)
        text = input('Continue playing (Y/N)? ')
        print()
        while text.upper() != 'N' and text.upper() != 'Y':
            text = input('Continue playing (Y/N)? ')
            print()
        if text.upper() == 'N':
            break
    display_stats(stats)


def play_round():
    """ Nonetype -> tuple

    Plays a single round of hangman from beginning to end. Returns a tuple\
    containing: the number of guesses, the number of correct guesses,\
    and the words.
    """

    counter = 0
    word = words.generate_word()
    guesses = set()
    correct_guesses = 0
    hangman = hangman_word(word, guesses)
    print()
    print(hangman)
    print()
    while hangman.count('_') != 0:
        counter += 1
        selected_letter = input('Please enter a letter: ').lower()
        if selected_letter not in guesses:
            guesses.add(selected_letter)
            hangman = hangman_word(word, guesses)
            print()
            print()
            print(hangman)
            print()
        else:
            print('\nDuplicate guess!\n')
            print(hangman)
            print()
        correct_guesses = len(word) - hangman.count('_')
    return (counter, correct_guesses, word)


def hangman_word(word, guesses):
    """ str, str -> str

    Given a string word, and a set of single letter guesses, returns a string,\
    all uppercase, each letter separated by a space. If the letter is not\
    present in guesses, then it is replaced with an underscore.

    >>> hangman_word('acres', {'a', 'r', 'c'})
    'A C R _ _ '
    >>> hangman_word('calm', {'i', 'c', 's'})
    'C _ _ _ '
    >>> hangman_word('film', {'o', 'i', 'l'})
    '_ I L _ '
    """

    output = ''
    for character in word:
        if character in guesses:
            output += character.upper() + ' '
        else:
            output += '_ '
    return output


def display_stats(stats):
    """ (dict of {str: int, str: in, str: str}) -> float

    Given a list of dicts, stats, display the statistics for one or more\
    rounds.

    >>> display_stats([{'correct': 5, 'word': 'brick', 'guesses': 5}])
    <BLANKLINE>
    Rounds: 1
    Average Guesses: 5.00
    Average Percent Correct: 100.0%
    Average Word Length: 5.00
    >>> display_stats([{'correct': 5, 'guesses': 12, 'word': 'lungs'},\
                      {'correct': 5, 'guesses': 15, 'word': 'acres'}])
    <BLANKLINE>
    Rounds: 2
    Average Guesses: 13.50
    Average Percent Correct: 37.5%
    Average Word Length: 5.00
    >>> display_stats([{'correct': 4, 'guesses': 14, 'word': 'film'},\
                      {'correct': 9, 'guesses': 17, 'word': 'fireplace'},\
                      {'correct': 5, 'guesses': 20, 'word': 'claws'}])
    <BLANKLINE>
    Rounds: 3
    Average Guesses: 17.00
    Average Percent Correct: 35.5%
    Average Word Length: 6.00
    """

    rounds = len(stats)
    average_guesses = 0
    average_percent_correct = 0
    average_word_length = 0
    for item in stats:
        average_guesses = average_guesses + item['guesses']
        average_percent_correct += item['correct'] / item['guesses']
        average_word_length = average_word_length + len(item['word'])
    print()
    print('Rounds: {}'.format(rounds))
    average_guesses = average_guesses / rounds
    print('Average Guesses: {:0.2f}'.format(average_guesses))
    average_percent_correct = (average_percent_correct / rounds) * 100
    print('Average Percent Correct: {:0.1f}%'.format(average_percent_correct))
    average_word_length = average_word_length / rounds
    print('Average Word Length: {:0.2f}'.format(average_word_length))


if __name__ == '__main__':
    main()
