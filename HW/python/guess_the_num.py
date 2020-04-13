
print('Hi! Lets play a game.')

secret_num = 58

guess = 0

count = 0

while guess != secret_num:
    guess = float(input('Guess which number from 0-100 am I thinking of: '))
    count += 1

    if guess > secret_num:
        print("No. it's lower than that.")

    if guess < secret_num:
        print("No, it's higher than that.")

else:
    print("Yes, that's it. Congratulation.", "You guessed in", count, "tries")
