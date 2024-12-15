def main():
    #Asks the user to enter a number and then squares that number.
    x = int(input("Give me a value for X: "))
    print("X squared is",square(x))

def square(x):
    return x*x

main()