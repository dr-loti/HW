
print('Hi, this is a unit converter, that converts km into miles or the other way around. \n')

while True:
    choice_1 = str(input('But first you have to choose. a) km > mi, or b) mi > km?: '))
    print("")
    if choice_1.lower() == "a":
        a = input("Ok. Now insert kilometers: ")

        a = float(a.replace(",", "."))

        mi = a * 0.621371
        print("")
        print(str(a) + " kilometers = " + str(mi) + " miles.")
        print("")

    elif choice_1 == "b":
        b = input("Ok. Now insert miles: ")

        b = float(b.replace(",", "."))

        km = b * 1.609344

        print(str(b) + " miles = " + str(km) + " kilometers.")

    else:
        print('Error.')

    choice_2 = input("Would you like to do another conversion (y/n): ")
    print("")
    if choice_2.lower() != "y" and choice_2.lower() != "yes":
        break