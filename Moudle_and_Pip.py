import If_Statement                                                                                 # We can import other files or libraries. CAREFUL!: Python imidiately executes the code

print("--------- Welcome to the ARCADE! ---------")
game = input("Choose your game\nGuessing Game (1)\nComing Soon (2)\nComing Soon (3)\n\n")
if game == "1":
    If_Statement.guessing_Game()                                                                    # That's how we access functions of a imported file/library
elif game == "2":
    print("Coming Soon")
elif game == "3":
    print("Coming Soon")

"""
Pip is a popular package manager that is basically a program that help to install
other third party modules for python
"""