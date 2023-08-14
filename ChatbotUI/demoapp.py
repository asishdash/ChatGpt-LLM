import openai
import flask
import os
import sys
import time
import random
from flask import Flask

openai.api_key = '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'

def chat_with_gpt():
    response =openai.ChatCompletion.create(
        model= "gpt-3.5-turbo",
        messages =[
            #this system is optional
            {"role":"system","content":"You are an AI architect , created an AI application on Machine Data and Machine logs "},
            #Ask your question
            {"role":"user","content":"create a quiz OF 20 QUESTIONS on the application and related AI with 4 options with answer"}
        ]
    )
    result=''
    for choice in response.choices:
        result += choice.message.content
    return result

def chat_with_gpt(prompt):
    model = 'text-davinci-002'
    response = openai.Completion.create(
        engine=model,
        prompt = prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=1
)
    return response.choices[0].text.strip()


if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("ChatGPT: Goodbye!")
            break
        response = chat_with_gpt(user_input)
        print("ChatGPT:", response)
