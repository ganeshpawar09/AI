import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, nice to meet you!"]
    ],
    [
        r"Hi|Hello|Hey there|Hola",
        ["Hey there! How can I assist you today?"]
    ],
    [
        r"what is your name ?",
        ["You can call me Bot!"]
    ],
    [
        r"how are you ?",
        ["I'm just a chatbot, so I'm always ready to assist you."]
    ],
    [
        r"sorry (.*)",
        ["It's okay. No worries!"]
    ],
    [
        r"I am fine",
        ["Glad to hear that! How can I help you today?"]
    ],
    [
        r"(.*) (good|great|awesome|amazing)",
        ["That's fantastic! How can I assist you further?"]
    ],
    [
        r"(.*) age?",
        ["I'm a chatbot, so I don't have an age."]
    ],
    [
        r"what (.*) want ?",
        ["I'm here to assist you with any questions or tasks you have."]
    ],
    [
        r"(.*) created ?",
        ["I was created by my developers using Python."]
    ],
    [
        r"(.*) (location|city) ?",
        ["I exist in the digital realm."]
    ],
    [
        r"how is weather in (.*)?",
        ["I'm not able to check the weather, but you can easily find out using a weather app or website."]
    ],
    [
        r"i work in (.*)?",
        ["That's interesting! What do you do at %1?"]
    ],
    [
        r"quit",
        ["Goodbye! Feel free to chat with me anytime."]
    ],
]

def chat():
    print("Hello! I'm Bot, your friendly chat assistant.")
    chatbot = Chat(pairs, reflections)
    chatbot.converse()

if __name__== "__main__":
    chat()
