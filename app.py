import os
from groq import Groq
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from typing import List, Dict

class ApiKeyManager:
    # Manages the API key for the Groq client.
    API_KEY = os.environ.get("GROQ_API_KEY")

class ContextualGroq:
    # Contextual Groq client for conversational AI.
    def __init__(self):
        # Initializes the ContextualGroq client.
        self.client = Groq(api_key=ApiKeyManager.API_KEY)
        self.conversation_history: List[Dict[str, str]] = []

    def interact_with_ai(self):
        # Interacts with the AI using the Groq client.
        while True:
            user_input = session.prompt('Enter your input (type "exit" to quit): ')

            if user_input.lower() == 'exit':
                break

            self.conversation_history.append({"role": "user", "content": user_input})

            chat_completion = self.client.chat.completions.create(
                messages=self.conversation_history,
                model="mixtral-8x7b-32768",
            )

            response = chat_completion.choices[0].message.content
            print(response)

            self.conversation_history.append({"role": "assistant", "content": response})

def validate_input(user_input: str) -> str:
    # Validates the user input.
    return user_input

def main():
    # Entrypoint of the application.
    session = PromptSession(history=FileHistory('history.txt'))
    contextual_groq = ContextualGroq()

    while True:
        user_input = validate_input(session.prompt('Enter your input (type "exit" to quit): '))

        if user_input.lower() == 'exit':
            break

        contextual_groq.interact_with_ai()

if __name__ == '__main__':
    session = PromptSession(history=FileHistory('history.txt'))
    contextual_groq = ContextualGroq()
    contextual_groq.interact_with_ai()