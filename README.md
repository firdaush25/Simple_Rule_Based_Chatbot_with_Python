
# 🤖 Simple Rule-Based Chatbot Using Python

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)
![Project Status](https://img.shields.io/badge/status-active-green)
![License](https://img.shields.io/badge/license-open--source-lightgrey)

A terminal-based chatbot built with Python that loads 100+ question-answer pairs from a JSON file. It asks for your name, responds intelligently to known prompts, and handles conversation in a friendly and personalized way. Perfect for learning CLI interaction and working with JSON-driven logic.

---

## 🧑‍💻 Author

**Firdaush Alam**  
📍 Python Developer Intern @ BroskiesHub  
🎓 Computer Science Engineer  
🔗 [Portfolio](https://firdaushalamportfolio.netlify.app/) | [LinkedIn](https://www.linkedin.com/in/firdaush-alam) | [GitHub](https://github.com/firdaush25)

---

## 🚀 Features

- ✅ Loads responses from `chatbot_responses.json`
- 🧑 Prompts for user name and uses it in conversation
- ❓ Requires questions to end with `?`
- 👋 Type `bye` to gracefully exit
- 💬 Handles over 100 common questions
- 🤷 Default reply for unrecognized input

---

## 🛠️ Getting Started

### 📦 Prerequisites

- Python 3.x installed

### 📥 Installation

```bash
git clone https://github.com/firdaush25/simple-python-chatbot
cd simple-python-chatbot
```

Ensure `chatbot_responses.json` is in the same directory as `chatbot.py`.

### ▶️ Usage

```bash
python chatbot.py
```

You’ll be prompted for:

- Your name  
- Instructions to use `?` at the end of questions  
- Type `bye` to exit

---

## 💬 Sample Interaction

```plaintext
A:\Broskies Hub internship\Task 8>python chatbot.py
Chatbot: Hi! I'm your simple chatbot.
May I know your Name. Firdaush
Hi Firdaush! Now U May ask your Questions.
Firdaush don't forget to Add ? after your Question
Firdaush, For exit type 'bye'
Ask: hi
Chatbot: Hi there! What can I do for you?
Ask: Hello
Chatbot: Hello! How can I assist you today?
Ask: how are you?
Chatbot: I'm a bot, but I'm doing well! How about you?
Ask: who discovered gravity?
Chatbot: Sir Isaac Newton is credited with gravitational theory.
Ask: what is the speed of light?
Chatbot: Approximately 299,792 kilometers per second.
Ask: how do I stay healthy
Chatbot: Sorry, I didn't understand that. Please try something else.
Ask: what careers involve coding?
Chatbot: Software development, data science, and more.
Ask: what is blockchain?
Chatbot: Blockchain is a distributed ledger for digital transactions.
Ask: can you tell me a fun fact?
Chatbot: Honey never spoils and can last thousands of years.
Ask: what is your purpose?
Chatbot: To help answer your questions using Python.
Ask: where is the nearest restaurant?
Chatbot: I don't have location info, try a map app.
Ask: how's the traffic?
Chatbot: I can't check traffic, try a navigation app.
Ask: bye
Chatbot: Goodbye! Have a great day!
```

---

## 📁 Project Structure

```
├── chatbot.py                  # Main Python script
├── chatbot_responses.json      # JSON file with Q&A pairs
└── README.md                   # Project documentation
```

---

## 🧠 How It Works

- Reads Q&A pairs from `chatbot_responses.json`
- Prompts user for name and stores it
- Loops to read and respond to user input
  - Matches questions with JSON keys
  - Gives default reply if no match
- Detects `"bye"` to end the chat

---

## 🌱 Future Improvements

- Add fuzzy matching and synonym support  
- Remove strict `?` requirement  
- Integrate NLP libraries (spaCy, NLTK, etc.)  
- Add emoji or markdown formatting (if GUI-based)

---

## 📢 Contributing

Feel free to fork this repository, open issues, or submit pull requests with enhancements, features, or new question-answer pairs.

---

## 📜 License

This project is open-source and free to use for educational and personal purposes.

---

## 🙌 Acknowledgements

- Inspired by beginner chatbot tutorials  
- Built with simplicity, personalization, and clean Python structure
