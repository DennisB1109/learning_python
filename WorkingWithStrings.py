from cmath import inf


print("Dennis lernt Python\n er ist noch am \"Anfang\"") # Creating new lines inside a string is done with '\n' 
                                                         # In order to use quotation marks inside a string we need to put a backslash in front of it

info = "We can also save strings inside variables" 
print(info + " and print them afterwards")              # Concatenation of strings with '+'
print(info.lower())                                     # transform whole string to lower case letters
print(info.isupper())                                   # checks if the string contains only upper letter -> returns True or False

print(info.upper().isupper())  

print(len(info))                                        # len is a function that takes a string and output the length of it

print(info.replace("save", "store"))                    # The replace function expexts two strings and replaces them (see context)
# Indexing
print(info[3])                                          # We can use an index to access a specific character of a string
print(info.index("vari"))                               # The index function expects a string (containing one or multiple characters) and returns the position of the string 