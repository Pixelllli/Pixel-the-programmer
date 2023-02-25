import random

# Define a dictionary of responses
responses = {
    "hi": ["Hello!", "Hi there!", "Hi!", "Hey!"],
    "how are you": ["I'm doing well, thanks for asking.", "I'm fine, how are you?", "Great!"],
    "what's your name": ["My name is ChatBot.", "You can call me ChatBot.", "I'm ChatBot!"],
    "default": ["Sorry, I didn't understand what you said.", "Could you please repeat that?", "I'm not sure what you mean."],
}

# Define a function to generate a response to user input
def respond(input_text):
    input_text = input_text.lower()
    for key in responses:
        if key in input_text:
            return random.choice(responses[key])
    return random.choice(responses["default"])

# Define the main loop for the chatbot
while True:
    user_input = input("You: ")
    bot_response = respond(user_input)
    print("Bot:", bot_response)
