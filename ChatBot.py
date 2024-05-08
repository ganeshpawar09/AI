import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    #
    [
        r"my name is (.*)",
        ["Hello %1, it's a pleasure to meet you."]
    ],
    # Or expression
    [
        r"Hi|Hello|Hey there|Hola",
        ["Hello! I'm ChatGPT, here to assist you."]
    ],
    [
        r"what is your name ?",
        ["You can call me ChatGPT!",]
    ],
    [
        r"how are you ?",
        ["I'm an AI, so I don't have feelings, but I'm functioning perfectly fine. How can I assist you today?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright. No need to apologize.",]
    ],
    [
        r"I am fine",
        ["That's great to hear! How can I assist you today?",]
    ],
    [
        r"(.*) (good|great|awesome|amazing)",
        ["I'm glad to hear that! How can I help you today?",]
    ],
    [
        r"(.*) age?",
        ["I'm an AI, so I don't age like humans do.",]
    ],
    [
        r"what (.*) want ?",
        ["I'm here to assist you and provide information to the best of my abilities.",]
    ],
    [
        r"(.*) created ?",
        ["I was developed by OpenAI using their GPT technology.",]
    ],
    [
        r"(.*) (location|city) ?",
        ['I exist in the realm of cyberspace.',]
    ],
    [
        r"how is weather in (.*)?",
        ["As an AI, I don't experience weather, but I can fetch you weather information for %1 if you want."]
    ],
    [
        r"i work in (.*)?",
        ["That's interesting! What do you do at %1?",]
    ],
    [
        r"quit",
        ["Thank you for chatting with me. If you have any more questions, feel free to ask!"]
    ],
]

def chat():
    print("Hey there! I'm ChatGPT, your friendly AI assistant.")
    chatbot = Chat(pairs, reflections)
    chatbot.converse()

if __name__== "__main__":
    chat()
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
