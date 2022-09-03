
colors = ["red", "green", "blue"]                    # Lists in python are so to say arrays
random = ["Hello", 24, True]                         # But in a list you can store all sorts of datatypes

print(colors[1])                                     # We can access the elements of the list through indexing
print(colors[-1])                                    # By indexing negatives, we index from the back of the list
print(colors[1:])                                    # with the : operator we access all elements after

colors[0] = colors[2]
print(colors[0])

# List functions
prime = [2, 3, 5, 7, 11, 17, 19, 23, 29]
print(prime)
prime.extend([31, 37, 41, 43])                      # The extend() function expects a list and appends it to the end of the list  
print(prime)
prime.append(47)                                    # The append() function expects a single element and appends it to the end of the list 
print(prime)
prime.insert(5, 13)                                 # The insert() function allows us to insert an element somewhere in the list
print(prime)
prime.remove(47)                                    # The remove() function allows us to remove an element from the list
print(prime)
random.clear()                                      # The clear() function deletes all elements of the list

alphabet = ["f", "j", "y", "s", "u", "j", "f", "b"]
alphabet.sort()                                     # The sort() function sorts a list in alphabetical and/or numerical ascending number
print(alphabet)
alphabet.reverse()
print(alphabet)                                     # The reverse() function reverses the elements of a list

new_prime = prime.copy()                            # Allows us to copy a list
print(new_prime)