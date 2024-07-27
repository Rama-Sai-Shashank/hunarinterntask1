import random
words=["python", "programming", "hangman", "development", "algorithm"]
selected_word=random.choice(words)
word_length=len(selected_word)
guessed_word=["_"]*word_length
guessed_letters=set()
max_incorrect_guesses=6
incorrect_guesses=0
def display_word():
    print("Current word:", " ".join(guessed_word))
def get_guess():
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) == 1 and guess.isalpha() and guess not in guessed_letters:
            guessed_letters.add(guess)
            return guess
        else:
            print("Invalid input. Please enter a single letter that you haven't guessed yet.")
def update_guessed_word(guess):
    for i, letter in enumerate(selected_word):
        if letter == guess:
            guessed_word[i] = guess
def check_win():
    return "_" not in guessed_word
print("Welcome to the Word Guessing Game!")
display_word()
while incorrect_guesses < max_incorrect_guesses and not check_win():
    guess = get_guess()
    if guess in selected_word:
        print("Correct guess!")
        update_guessed_word(guess)
    else:
        incorrect_guesses+=1
        print(f"Incorrect guess. You have {max_incorrect_guesses - incorrect_guesses} guesses left.")
    display_word()
if check_win():
    print("Congratulations! You've guessed the word:", selected_word)
else:
    print("Sorry, you've run out of guesses. The word was:", selected_word)
