# Simple FAQ Chatbot (Console Version)
def process_input(user_input):
    """
    Process the user input to determine the intent and return an appropriate response.
    """
    user_input = user_input.lower().strip()

    # Define variations for each intent
    greeting_variations = ["hello", "hi", "good day", "hey"]
    product_variations = ["services", "what do you offer", "service offerings", "services offered"]
    pricing_variations = ["cost", "price", "how much", "pricing", "charge"]
    support_variations = ["support", "contact", "customer support", "help"]

    # Check for each intent using simple keyword search
    if any(phrase in user_input for phrase in greeting_variations):
        return "Hello! How can I assist you today?"
    elif any(phrase in user_input for phrase in product_variations):
        return "We offer a range of services including web development, mobile app development, and digital marketing."
    elif any(phrase in user_input for phrase in pricing_variations):
        return "Our pricing varies by service. Could you specify which service you are interested in?"
    elif any(phrase in user_input for phrase in support_variations):
        return "You can reach our customer support at support@example.com or call us at +1-234-567-890."
    else:
        return "I'm sorry, I didn't understand that. Could you please rephrase your query?"

print("Welcome to the FAQ Chatbot! (Type 'exit' to end the conversation)")

# Chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = process_input(user_input)
    print("Chatbot:", response)
