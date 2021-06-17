import random
import time

print("Greetings and welcome to Hangman game!")
time.sleep(2)
players_name = input("What is your name? ")
if 3 < len(players_name) < 10 and players_name.isalpha():
    print(f"Greetings and welcome, {players_name}. I want to play a game.")
    game_started = True
else:
    real_name = input("Don't try to fool me. What is your real name? ")
    if 3 < len(real_name) > 10 and real_name.isalpha():
        print(f"Greetings and welcome, {players_name}. I want to play a game.")
    else:
        print("Don't come back, liar.")
        exit()
print("You will have 5 guesses at the beginning of the game.")
time.sleep(3)


def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = [
        "pillow", "change", "needle", "threat", "inside", "remedy", "weight", "revise", "honest", "sodium", "future",
        "lonely", "insist", "packet", "suburb", "repeat", "planet", "dragon", "string", "pocket", "jockey", "candle",
        "reveal", "demand", "player", "snatch", "aspect"]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""


def play_loop():
    global play_game
    play_game = input('Do you want to play a game? y = yes, n = no')
    while play_game not in ["y", "n", "Y", "N"]:
        play_game = input("Do you want to play again? y = yes, n = no \n")
    if play_game == "y":
        main()
    elif play_game == "n":
        print("Thank you for playing.")
        exit()


def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    guess_limit = 5
    guess = input("This is a Hangman word:" + display + " Enter your guess:\n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid input. Try a letter.\n")
        hangman()
    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

    elif guess in already_guessed:
        print("Try another letter.\n")

    else:
        count += 1

        if count == 1:
            time.sleep(2)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(guess_limit - count) + " guesses remaining\n")
        elif count == 2:
            time.sleep(2)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(guess_limit - count) + " guesses remaining\n")
        elif count == 3:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(guess_limit - count) + " guesses remaining\n")
        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(guess_limit - count) + " last guess remaining\n")
        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:", word, already_guessed)
            play_loop()
    if word == '_' * length:
        print("Congrats! You have guessed the word correctly!")
        play_loop()
    elif count != guess_limit:
        hangman()


main()
hangman()
