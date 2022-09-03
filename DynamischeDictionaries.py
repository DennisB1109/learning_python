#Erstellen ein leeres Dictionary
car_specs = {}

#Erstellen einer Liste welche die selbe Anzahl an Elementen hat wie der User Autos haben will
amount = float(input("How many cars do you want to create?\n"))
if(amount == 0):
    quit()
else:
    dict_list = [amount]
    temp = amount
    while amount > 1:
        amount -= 1
        dict_list.append(amount)
    amount = temp

#Hier wird das leere Dictionary initialisiert
iterator = 0
while iterator != amount:
    brand = input("Input the cars Brand: ")
    construction_year = input("Input the construction year of the car: ")
    color = input("Input the color of the car: ")
    car_specs["Brand"] = brand
    car_specs["Construction year"] = construction_year
    car_specs["Color"] = color
    print(car_specs)
    dict_list[iterator] = car_specs                             #Goal: safe Dictionary as an Element of the List (doesn't work)
    iterator += 1

print("\nYour List of Cars")
for test in dict_list:
    print(test)
