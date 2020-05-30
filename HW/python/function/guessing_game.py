
import datetime
import json
import random

# A
def play_game():
    secret = random.randint(1, 30)
    attempts = 0
    gamer = input("Hi, let's play a game, but first enter your name: ")
    score_list_dy = get_score_list()


    while True:
        guess = int(input("Guess the secret number (between 1 and 30): "))
        attempts += 1

        if guess == secret:
            score_list_dy.append({"player_name": gamer,
                                  "attempts": attempts,
                                  "date": str(datetime.datetime.now()),
                                  "secret_number": secret})

            with open("score_list_dy.txt", "w") as score_file:
                score_file.write(json.dumps(score_list_dy))

            print("You've guessed it - congratulations! It's number " + str(secret))
            print("Attempts needed: " + str(attempts))
            break

        elif guess > secret:
            print("Your guess is not correct... try something smaller")
        elif guess < secret:
            print("Your guess is not correct... try something bigger")


def get_score_list():
    with open("score_list_dy.txt", "r") as score_file:
        score_list_dy = json.loads(score_file.read())

        return score_list_dy

# B
def get_top_scores():
    score_list_dy = get_score_list()
    top_scores = sorted(score_list_dy, key=lambda k: k['attempts'])[:3]

    return top_scores

while True:
    selection = input("Choose the correct letter, wisely. Would you like to "
                      "A) play a new game, B) se the best scores, or C) quit the game? ")

    if selection.upper() == "A" or selection.lower() == "a":
        play_game()

    elif selection.upper() == "B" or selection.lower() == "b":
        for score_dict in get_top_scores():
            print("Top 3 scores: " '\n' "Player " + score_dict.get("player_name") + " made " + str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date") + ". The secret number was: " + str(score_dict["secret_number"]))

    else:
        break

#play_game(level="hard")

#play_game(level="easy")
