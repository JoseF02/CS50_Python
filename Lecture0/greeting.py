def greet(input):
    if "hello" in input.lower():
        return "hello, there"
    else:
        return "I'm not sure what you mean"

greeting = greet("HelLo, Computer")
print(greeting)