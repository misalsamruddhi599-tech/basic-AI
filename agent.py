print("Basic AI Agent")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Agent: Hello! How can I help you?")

    elif user == "how are you":
        print("Agent: I am fine. Thank you!")

    elif user == "name":
        print("Agent: My name is Basic AI Agent.")

    elif user == "help":
        print("Agent: You can type hello, how are you, name, or bye.")

    elif user == "bye":
        print("Agent: Goodbye!")
        break

    else:
        print("Agent: Sorry, I don't understand.")