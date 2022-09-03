from ctypes import sizeof


secretWord = "Python"
guesses = []
usersWord = ""

while usersWord != secretWord:
    print("I'm thinking of a word, can you guess which one?")
    usersWord = input("Make a GUESS!: ")
    guesses.append(usersWord)
    print(usersWord)
    print("These are your guesses so far ", guesses)

print("You guessed it correct! It took you ", len(guesses), "guesses")