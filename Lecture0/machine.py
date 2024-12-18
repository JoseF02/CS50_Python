emoticon = "v.v"

def main():
    global emoticon     
    say("It's anyone there?")
    emoticon = ":D"
    say("Oh, hi!")

def say(phrase):
    print(phrase + " " + emoticon)

main()