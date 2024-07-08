import random

print("- Welcome to my game. I wish you lots of luck, for it is very hard :-)")
top_range = input("- Please type a upper limit number: ")

if top_range.isdigit():
    top_range = int(top_range)
    if top_range <= 0:
        print("- Please type number greater than 0.")
        quit()
else:
    print("Please type a number!")
    quit()

random_number = random.randint(0, top_range)
guesses = 0

while True:
    guesses += 1
    player_guess = input("- Please make a guess: ")
    if player_guess.isdigit():
        player_guess  = int(player_guess)

    else:
        print("- This input won't work. Please type a number!")
        continue

    if player_guess == random_number:
        print("- Congratulations. You guessed it right!")
        break

    elif player_guess > random_number:
            print("- Your guess was above the number!")
    else:
            print("- Your guess was below the number!")


print("- You guessed it in", guesses, "guesses")
print("- Thank you for playing. See you soon for another round :-)!")

