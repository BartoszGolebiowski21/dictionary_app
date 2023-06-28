from enum import IntEnum
from functions import load_json_file, save_json_file, translate, add_new_word, edit_translation, show_dictionary, draw_word, check_answer


commands = IntEnum('Menu', 'Translate Add Edit Show Test Exit')

while True:
    try:
        english_dictionary = load_json_file()
        command = int(input("""
1. Translate
2. Add new word
3. Edit translation
4. Show entire dictionary
5. Test mode
6. Exit
Choice:
"""))
        if command == commands.Translate:
            word = (input("Enter the word to translate:\n"))
            translate(english_dictionary, word)

        elif command == commands.Add:
            added_word = (input("Enter the word in English:\n"))
            added_translation = (input("Enter the translation in Polish:\n"))
            add_new_word(english_dictionary, added_word, added_translation)
            save_json_file(english_dictionary)

        elif command == commands.Edit:
            word = (input("Enter the word to edit:\n"))
            edited_translation = (input("Enter the translation in Polish:\n"))
            edit_translation(english_dictionary, word, edited_translation)
            save_json_file(english_dictionary)

        elif command == commands.Show:
            show_dictionary(english_dictionary)

        elif command == commands.Test:
            drawn_word = draw_word(english_dictionary)
            number_of_remaining_repetitions = english_dictionary[drawn_word]['repetitions']
            if number_of_remaining_repetitions > 0:
                print("Word to translate:\n",drawn_word)
                user_translation = (input("Enter the translation in Polish:\n"))
                correct_translation = english_dictionary[drawn_word]['translation']
                check_answer(english_dictionary, drawn_word, user_translation, correct_translation)
                save_json_file(english_dictionary)
            else:
                # poniżej wyrażenie generujące - generuje liczbę 1 jeśli program znajdzie wartość 0 dla "repetitions"
                repetitions_zero_count = sum(1 for word_data in english_dictionary.values() if word_data['repetitions'] == 0)
                if repetitions_zero_count == len(english_dictionary):
                    print("You have studied all the words")
                    save_json_file(english_dictionary)
                    break
                else:
                    continue

        elif command == commands.Exit:
            break

        else:
            print("Incorrect choice")
    except ValueError:
        print("Incorrect choice")
