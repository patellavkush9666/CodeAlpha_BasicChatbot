print("===================================")
print("       WELCOME TO PYTHON BOT")
print("===================================")
print("You can talk to me!")
print("Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower().strip()

    if user_input in ["hello", "hi", "hey"]:
        print("Bot: Hello! Welcome to my chatbot.")

    elif user_input == "how are you":
        print("Bot: I am fine, thank you!")

    elif user_input in ["what is your name", "your name"]:
        print("Bot: I am Python Bot.")

    elif user_input in ["what can you do", "help"]:
        print("Bot: I can answer simple messages.")

    elif user_input in ["thank you", "thanks"]:
        print("Bot: You're welcome!")

    elif user_input == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that yet.")