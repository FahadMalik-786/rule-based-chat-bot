import random
from datetime import datetime

class ChatBot:
    """
    A simple rule-based chatbot with greetings, questions, farewells,
    and a help command.
    """

    def __init__(self):
        self.responses = {
            "greetings": ["hello", "hi", "hey"],
            "farewells": ["bye", "goodbye", "see you", "quit", "exit"],
            "questions": {
                "how are you": [
                    "I'm doing great, thanks for asking!",
                    "I’m just a bot, but I’m feeling good. How about you?",
                    "All systems running smoothly 😊"
                ],
                "what is your name": [
                    "I'm PyBot 🤖",
                    "You can call me ChatBot.",
                    "I’m your Python chatbot assistant!"
                ],
                "what can you do": [
                    "I can chat with you and keep you company!",
                    "I respond to greetings, farewells, and simple questions.",
                    "Try typing 'help' to see my commands 🚀"
                ]
            }
        }

    def time_based_greeting(self) -> str:
        """Return greeting based on current time."""
        hour = datetime.now().hour
        if hour < 12:
            return "Good morning! ☀️"
        elif hour < 18:
            return "Good afternoon! 🌤️"
        else:
            return "Good evening! 🌙"

    def get_response(self, user_input: str) -> str:
        """Generate a response based on user input."""
        user_input = user_input.lower().strip()

        # Farewell detection
        if user_input in self.responses["farewells"]:
            return random.choice(["Goodbye 👋", "See you soon!", "Bye, take care!"])

        # Greeting detection
        if user_input in self.responses["greetings"]:
            return random.choice(["Hello there!", "Hey! How’s it going?", self.time_based_greeting()])

        # Help command
        if user_input == "help":
            return "I can respond to greetings, farewells, and simple questions like:\n- how are you\n- what is your name\n- what can you do"

        # Question detection
        for question, answers in self.responses["questions"].items():
            if question in user_input:
                return random.choice(answers)

        # Default response
        return random.choice([
            "Hmm, I’m not sure I understand 🤔",
            "Can you rephrase that?",
            "Interesting! Tell me more..."
        ])

    def run(self):
        """Start the chatbot loop."""
        print("🤖 PyBot: Hello! Type 'bye' or 'exit' to quit.")
        while True:
            user_input = input("You: ")
            response = self.get_response(user_input)
            print("🤖 PyBot:", response)
            if user_input.lower().strip() in self.responses["farewells"]:
                break


if __name__ == "__main__":
    bot = ChatBot()
    bot.run()
