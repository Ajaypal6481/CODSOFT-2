import re
from nltk.corpus import wordnet

# Load keywords, synonyms, intents, and responses from data files
keywords = {}
with open('data/keywords.txt', 'r') as f:
    for line in f:
        keyword, synonyms = line.strip().split(':')
        keywords[keyword] = [synonym.strip() for synonym in synonyms.split(',')]

intents = {}
with open('data/intents.txt', 'r') as f:
    for line in f:
        intent, keywords = line.strip().split(':')
        intents[intent] = [keyword.strip() for keyword in keywords.split(',')]

responses = {}
with open('data/responses.txt', 'r') as f:
    for line in f:
        intent, response = line.strip().split(':')
        responses[intent] = response.strip()

# Compile regular expressions for each intent
keywords_dict = {}
for intent, keywords in intents.items():
    keywords_dict[intent] = re.compile('|'.join(['.*\\b' + keyword + '\\b.*' for keyword in keywords]))

# Define the chatbot's main function
def chatbot(user_input):
    user_input = user_input.lower()
    matched_intent = None
    for intent, pattern in keywords_dict.items():
        if re.search(pattern, user_input):
            matched_intent = intent
    key = 'fallback' if matched_intent is None else matched_intent
    return responses[key]

# Test the chatbot
print("Welcome to MyBank. How may I help you?")
while True:
    user_input = input().lower()
    if user_input == 'quit':
        print("Thank you for visiting.")
        break
    print(chatbot(user_input))
