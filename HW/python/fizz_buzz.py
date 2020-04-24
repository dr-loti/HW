
print('Hi, lets play a game, caled FizzBuzz. \n')

num = int(input("Select a number between 1 and 100: "))
print("")
for x in range (1, num+1):

    if x % 3 == 0 and x % 5 == 0:
        print("fizzbuzz")

    elif x % 3 == 0:
        print("fizz")

    elif x % 5 == 0:
        print("buzz")

    else:
        print(x)
