import json
import os
import random

current_directory = os.path.dirname(os.path.abspath(__file__))
json_file_path = os.path.join(current_directory, "vocabulary_bank.json")

def load_json_file():
    with open(json_file_path, "r", encoding="UTF-8") as file:
        return json.load(file)
    
def save_json_file(data):
    with open(json_file_path, "w", encoding="UTF-8") as file:
        return json.dump(data, file, ensure_ascii=False)

def translate(dictionary, word):
    if word in dictionary:
        translation = dictionary[word]['translation']
        print(word, "-", translation)
    else:
        print("The word '",word,"' isn't in the dictionary. You may add it.")

def add_new_word(dictionary, added_word, added_translation):
    if added_word in dictionary:
        print("The word '",added_word,"' has been already added into the dictionary")
    else:
        dictionary[added_word] = {'translation': added_translation, 'repetitions': 5}
        print("The word '",added_word,"' has been added succesfully")

def edit_translation(dictionary, word, edited_translation):
    if word in dictionary:
        dictionary[word] = {'translation': edited_translation, 'repetitions': 5}
        print("The word '",word,"' has been edited succesfully")
        print(word, "-", edited_translation)
    else:
        print("The word '",word,"' isn't in the dictionary")

def show_dictionary(dictionary):
    for word, translation in sorted(dictionary.items()):
        print(word, "-", translation)

def draw_word(dictionary):
    words_list = tuple(dictionary.keys())
    random_word = random.choice(words_list)
    return random_word

def check_answer(dictionary, drawn_word, user_answer, correct_answer):
    if user_answer == correct_answer:
        print("Correct answer!")
        dictionary[drawn_word]['repetitions'] -= 1
    elif user_answer != correct_answer:
        print("Incorrect answer. The correct translation is:\n",correct_answer)
