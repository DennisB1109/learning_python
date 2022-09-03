"""
With the input function we can get a user input that is by default seen as a string. So be carefull when working with numbers as user input (you have to convert it)
In the parantheses we can add a Text that appear infront of the user input.

"""
bank_Institute = input("Enter Bank Institute: ")
card_Number = input("Enter Cardnumber: ")           
print("Are the typed in informations correct?\nInstitute: " + bank_Institute + "\nBanknumber: " + card_Number)