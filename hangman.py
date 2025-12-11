import random

HANGMAN_STAGES = [
    """
       ------
       |    |
       |
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    --------
    """
]

WORDS = [
    "python", "hangman", "programming", "computer", "keyboard",
    "developer", "algorithm", "function", "variable", "database",
    "software", "internet", "application", "interface", "debugging"
]


def get_random_word():
    return random.choice(WORDS).upper()


def display_word(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)


def play_hangman():
    word = get_random_word()
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong = len(HANGMAN_STAGES) - 1

    print("\n" + "=" * 40)
    print("       WELCOME TO HANGMAN!")
    print("=" * 40)

    while wrong_guesses < max_wrong:
        print(HANGMAN_STAGES[wrong_guesses])
        print(f"Word: {display_word(word, guessed_letters)}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        print(f"Remaining attempts: {max_wrong - wrong_guesses}")

        guess = input("\nGuess a letter: ").upper().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter!")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good job! '{guess}' is in the word!")
            if all(letter in guessed_letters for letter in word):
                print("\n" + "=" * 40)
                print(f"  CONGRATULATIONS! You won!")
                print(f"  The word was: {word}")
                print("=" * 40)
                return True
        else:
            wrong_guesses += 1
            print(f"Wrong! '{guess}' is not in the word.")

    print(HANGMAN_STAGES[wrong_guesses])
    print("\n" + "=" * 40)
    print(f"  GAME OVER! You lost!")
    print(f"  The word was: {word}")
    print("=" * 40)
    return False


def main():
    while True:
        play_hangman()
        play_again = input("\nPlay again? (y/n): ").lower().strip()
        if play_again != 'y':
            print("Thanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    main()
