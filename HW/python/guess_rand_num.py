
print('Hi! Lets play a game.')

from random import randint

x = randint(0, 100)

number = 0

count = 0

while number != x:
    number = float(input('Which number in between 0 and 99 do I have? '))
    count += 1

    if number > x:
        print ("Lower")

    if number < x:
        print("Higher")

else:
    print("Yes, that's it. It's number " + str(x), "congratulation, you guessed in", count, "tries.")