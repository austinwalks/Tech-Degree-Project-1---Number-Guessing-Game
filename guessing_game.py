
import random
from statistics import mean, median, mode

def start_game():
    hidden_number = random.randint(1, 100)
    guesses = 0
    correct_score = []
    player_name = input("Welcome! What is your name? ")
    print("Hello, " + player_name,"!")
    play_game = input("Would you like to play? Yes/no  ")

    while play_game:
        guess_a_number = input("Choose a number  >  ")
        guesses += 1
        try:
            guess_a_number = int(guess_a_number)
            if guess_a_number <= 0:
                print("Please choose a number between 1 and 100.")
                continue
            elif guess_a_number > 100:
                print("Please choose a number between 1 and 100.")
                continue
            pass
        except ValueError:
            print("Huh? That is not a valid number! Please try again.")
            continue
        if guess_a_number == hidden_number:
            correct_score.append(guesses)
            correct_score.sort()
            print("Got it!")
            print("It took you {} guesses.".format(guesses))
            play_game = input("Would you like to play again? Yes/no  ")
            if correct_score:
                print("So far, no one's been able to to be the all-time high score. Which is {} guesses!".format(correct_score[0]))
            if play_game.lower() == 'no':
                print("Aw okay; Well, I'm around so come by again to play if you feel bored. See you soon!")

                print(f"Number of tries: {len(correct_score)}")
                print(f"All Scores: {correct_score}")
                mode_score = mode(correct_score)
                print(f"Your mode is: {mode_score}")
                median_score = median(correct_score)
                print(f"Your median is: {median_score}")
                mean_score = mean(correct_score)
                print(f"Your mean is: {round(mean_score,2)}")

                break
            else:
                guesses = 0
                hidden_number = random.randint(1, 100)
        elif guess_a_number < hidden_number:
            print("Your guess was too low. The number I'm thinking of is higher. Try again.")
            continue
        elif guess_a_number > hidden_number:
            print("Your guess was too high. The number I'm thinking of is lower. Give it another shot.")
            continue

start_game()
