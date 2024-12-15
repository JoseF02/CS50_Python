def call():
    #Ask the user for their name
    name = input("Whats your name? ")
    hello(name)

def hello(name="World"):
    #Remove whitespace from the str and capitalize each word of the str
    name = name.strip().title()

    #Split user name into first name and last name 
    parts = name.split()
    first, last = parts[0], parts[1] if len(parts) > 1 else ""

    #Show a message saying hello to the user
    print(f"Hello , {first} {last}") 

call()
