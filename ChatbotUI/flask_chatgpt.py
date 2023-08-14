from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)
app.secret_key = 'your_secret_key'

openai.api_key = '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'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    model ="text-davinci-002"
    print("we are here")
    user_message = request.json['message']
    response = openai.Completion.create(
        engine=model,
        prompt = user_message,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=1
)
    chatbot_response = response.choices[0].text.strip()
    return jsonify({'response': chatbot_response})

@app.route('/chatreroute', methods=['POST'])
def chatreroute():
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
    return jsonify({'response': result})

@app.route('/chatget', methods=['GET'])
def chatget():
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
    return jsonify({'response': result})

if __name__ == '__main__':
    app.run(debug=True)
