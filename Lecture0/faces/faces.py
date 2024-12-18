def main():
    phrase = input("")
    print(respond(phrase))

def respond(phrase):
    if phrase=="Hello :)":
        return "Hello 🙂"
    elif phrase=="Goodbye :(":
        return "Goodbye 🙁"
    elif phrase=="Hello :) Goodbye :(":
        return "Hello 🙂 Goodbye 🙁"

main()

