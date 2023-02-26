import openai
import os


class Chatbot:
    def __init__(self):
        openai.api_key = "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"

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=4000,
            temperature=0.5,     # sets how accurate the answer will be, from 0 to 1
        ).choices[0].text
        return response


if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("explain python simply")
    print(response)

