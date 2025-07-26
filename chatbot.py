import json

# Load responses from JSON file
with open("chatbot_responses.json", "r") as file:
    responses = json.load(file)

print("Chatbot: Hi! I'm your simple chatbot.")
user_name = input(str("May i know your Name.")).capitalize()
print(f"Hi {user_name}! Now U May ask your Questions.")
print(f"{user_name} don't forget to Add ? after your Question")
print(f"{user_name}, For exit type 'bye'")

while True:
    user_input = input("Ask: ").lower().strip()
    if user_input == "bye":
        print("Chatbot:", responses.get("bye", "Goodbye!"))
        break
    elif user_input in responses:
        print("Chatbot:", responses[user_input])
    else:
        print("Chatbot: Sorry, I didn't understand that. Please try something else.")
