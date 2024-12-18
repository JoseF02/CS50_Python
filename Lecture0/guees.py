def get_guess():
    guess = int(input("Guess the number: "))
    return guess

def user_guess():
    guess = get_guess()
    if  guess == 50:
        print("Congrats, you guessed the number")
    else:
        print(f"Wrong, the number was 50")

user_guess()