def chatbot():
    responses = {
        "hello": "Hi there! How can I help you?",
        "bye": "Goodbye! Have a great day!",
        "how are you": "I’m just a bot, but I’m doing fine. How about you?"
    }

    while True:
        user_input = input("You: ").lower()
        if user_input in responses:
            print("Bot:", responses[user_input])
        else:
            print("Bot: Sorry, I don’t understand that.")
        if user_input == "bye":
            break

chatbot()
