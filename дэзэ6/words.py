import re

words = input()

def find_words(text):
    result = re.findall(r"\b[а-яёА-ЯЁa-zA-Z-]+", text)
    return result

print(len(find_words(words)))