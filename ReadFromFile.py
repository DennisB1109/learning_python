friends_file = open("Friends.txt", 'r')                                        # The open function allows you to open a text file ("File_Name", 'mode (r/w/a/r+)')

print(friends_file.readable())                                                 # readable() checks if a function is readable (returns a boolean)
#print(friends_file.read())                                                    # Outputs everything inside the opened file
#print(friends_file.readlines())                                               # Creates a list where each line of the file is a element of the list
#print(friends_file.readlines()[1])                                            # We can access each line through indexing

friends_file.close()                                                           # Whenever we open a file we eventually have to close it 

new_file = open("MyHtml.html", 'w')                                            # With the write mode 'w' we can also create new files
new_file.write("<!DOCTYPE html>\n<html>\n<body\n<h1>This is heading 1</h1>\n</body>\n</html>")  #Like this we can create for example a HTML file thorugh python
new_file.close()