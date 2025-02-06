import streamlit as st

def get_response(user_input):
    """
    Process the user input to determine the intent and return an appropriate response.
    """
    user_input_lower = user_input.lower().strip()
    
    # Define variations for each intent
    greeting_variations = ["hello", "hi", "good day", "hey"]
    product_variations = [
        "what services do you offer",
        "services",
        "what do you offer",
        "service offerings",
        "services offered"
    ]
    pricing_variations = [
        "what is the cost",
        "price",
        "how much",
        "pricing",
        "charge"
    ]
    support_variations = [
        "customer support",
        "support",
        "contact",
        "help"
    ]
    
    # Check for greeting intent
    if any(phrase in user_input_lower for phrase in greeting_variations):
        return "Hello! How can I assist you today?"
    # Check for product information intent
    elif any(phrase in user_input_lower for phrase in product_variations):
        return ("We offer a variety of services including web development, mobile app development, "
                "and digital marketing. Let me know if you need more details!")
    # Check for pricing information intent
    elif any(phrase in user_input_lower for phrase in pricing_variations):
        return ("Our pricing is competitive and varies based on the service and scope of the project. "
                "Could you please specify which service you're interested in?")
    # Check for support contact intent
    elif any(phrase in user_input_lower for phrase in support_variations):
        return ("You can reach our customer support at support@example.com or call us at +91-1234-567-890. "
                "We're here to help!")
    else:
        return "I'm sorry, I didn't understand that. Could you please rephrase your query?"

# Streamlit app interface
st.title("Simple Chatbot")
st.write("Welcome! Ask any questions you have about our services below.")

# Get user input from a text field
user_input = st.text_input("You: ", "")

# Check user input and respond accordingly
if user_input:
    if user_input.lower().strip() == "exit":
        st.markdown("**Chatbot:** Have a nice day, Goodbye!")
    else:
        response = get_response(user_input)
        st.markdown(f"**Chatbot:** {response}")