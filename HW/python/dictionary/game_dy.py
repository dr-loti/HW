
import datetime
import json
import random

secret = random.randint(1, 30)
attempts = 0

gamer = input("Hi, let's play a game, but first enter your name: ")

with open("score_list_dy.txt", "r") as score_file:
    score_list_dy = json.loads(score_file.read())
    #print("Top scores: " + str(score_list_dy))

top_scores = sorted(score_list_dy, key=lambda k: k['attempts'])[:3]

for score_dict in top_scores:
    score_text = "Player {0} had {1} attempts on {2}. The secret number was {3}. {4} guesses were wrong.".format(score_dict.get("player_name"),
                                                                                                                str(score_dict.get("attempts")),
                                                                                                                score_dict.get("date"),
                                                                                                                str(score_dict.get("secret_number")),
                                                                                                                score_dict.get("wrong_g"))

wrong_g = []

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        score_list_dy.append({"attempts": attempts,
                              "date": str(datetime.datetime.now()),
                              "player_name": gamer,
                              "secret_number": secret,
                              "wrong_guesses": wrong_g})

        with open("score_list_dy.txt", "w") as score_file:
            score_file.write(json.dumps(score_list_dy))


        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")

    wrong_g.append(guess)

print(score_text)