# Define a function to respond to user inputs
def simple_chatbot(user_input):
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Define predefined rules and responses
    responses = {
        "hello": "Hello! How can I help you?",
        "how are you": "I'm just a computer program, but I'm here to assist you!",
        "what is your name": "I'm a simple chatbot. You can call me ChatGPT.",
        "bye": "Goodbye! If you have more questions, feel free to ask anytime.",
    }

    # Check if the user input matches any predefined rule
    for keyword, response in responses.items():
        if keyword in user_input:
            return response

    # If no rule matches, provide a default response
    return "I'm sorry, I don't understand. Can you please rephrase your question?"

# Main chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = simple_chatbot(user_input)
    print("Chatbot:", response)
