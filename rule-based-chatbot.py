import random

class ChatBot:
    def __init__(self):
        self.responses = {
            "greetings": ["hello", "hi", "hey", "good morning", "good evening"],
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
                    "I don’t have a fancy name, just your friendly bot."
                ],
                "what can you do": [
                    "I can chat with you and keep you company!",
                    "Right now, I respond to basic questions and greetings.",
                    "I’m learning more every day 🚀"
                ]
            }
        }

    def get_response(self, user_input: str) -> str:
        user_input = user_input.lower().strip()

        # Farewell detection
        if user_input in self.responses["farewells"]:
            return random.choice(["Goodbye 👋", "See you soon!", "Bye, take care!"])

        # Greeting detection
        if user_input in self.responses["greetings"]:
            return random.choice(["Hello there!", "Hey! How’s it going?", "Hi 👋"])

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
