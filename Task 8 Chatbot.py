

import re
from datetime import datetime
import random


def normalize(text: str) -> str:
    """Lowercase, remove punctuation, collapse spaces."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s]", " ", text)   # remove punctuation
    text = re.sub(r"\s+", " ", text)       # collapse multiple spaces
    return text


def respond(user_message: str) -> str:
    """Return a response using only if/elif/else rules."""
    msg = normalize(user_message)

    # 1) Greetings
    if ("hi" in msg or "hello" in msg or "hey" in msg or
        "good morning" in msg or "good afternoon" in msg or "good evening" in msg):
        greetings = [
            "Hello! 👋",
            "Hi there! How can I help you today?",
            "Hey! I'm here to chat."
        ]
        return random.choice(greetings)

    # 2) Bot identity
    elif "your name" in msg or "who are you" in msg:
        return "I'm a simple rule-based Python chatbot built with if/elif/else."

    # 3) Help prompt
    elif "help" in msg:
        return ("You can try: 'time', 'date', 'joke', 'who are you', 'thanks', "
                "or say 'bye' to exit.")

    # 4) Time
    elif "time" in msg:
        return "Current time is " + datetime.now().strftime("%I:%M %p")

    # 5) Date / Day
    elif "date" in msg or "day" in msg:
        return "Today is " + datetime.now().strftime("%A, %d %B %Y")

    # 6) Jokes
    elif "joke" in msg:
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "I told my computer I needed a break, and it said: 'No problem, I'll go to sleep.'",
            "There are 10 kinds of people: those who understand binary and those who don't."
        ]
        return random.choice(jokes)

    # 7) Thanks
    elif "thanks" in msg or "thank you" in msg or "thank" in msg:
        return "You're welcome! 😊"

    # 8) Farewells / exit
    elif ("bye" in msg or "goodbye" in msg or "see you" in msg or
          "exit" in msg or "quit" in msg):
        return "Goodbye! 👋 See you next time."

    # 9) Fallback
    else:
        return "I didn't get that. Type 'help' to see what I understand."


def main() -> None:
    print("=" * 56)
    print(" Simple Rule-based Chatbot (Task 8) ")
    print(" Type 'help' for options, and 'bye' to exit.")
    print("=" * 56)

    while True:
        user = input("You: ")
        bot = respond(user)
        print(f"Bot: {bot}")

        # Exit condition after response
        msg = normalize(user)
        if ("bye" in msg or "goodbye" in msg or "see you" in msg or
                "exit" in msg or "quit" in msg):
            break


if __name__ == "__main__":
    main()
