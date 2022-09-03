monthconversion = {                                         # Here we define a structure called "Dictionary"
    "Jan" : "January",                                      # All  this values are called "Key-Value Pairs". They have to be unique
    "Feb" : "Febraury",
    "Mar" : "March",
    "Apr" : "April",
    "Mai" : "Mai",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sep" : "September",
    "Okt" : "Oktober",
    "Nov" : "November",
    "Dez" : "Dezember"
}

month = input("Input a month abbreviation: ")
print(monthconversion.get(month, "Not a valid Key"))

"""
Very Simple Stuff
"""