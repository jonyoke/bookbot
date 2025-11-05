def get_num_words(long_string):
    return len(long_string.split())

def get_num_characters(long_string):
    lowercase_string = long_string.lower()
    character_counter = {}
    for i in range(0, len(lowercase_string)):
        character = lowercase_string[i]
        if character not in character_counter:
            character_counter[character] = 1
        else:
            character_counter[character] = character_counter[character] + 1
    return character_counter

def return_num_from_dict(dict):
    return dict["num"]

def sort_character_counter(character_counter):
    list_of_character_counters = []
    for key, value in character_counter.items():
        dict = {}
        dict["char"] = key
        dict["num"] = value
        list_of_character_counters.append(dict)
    #print(list_of_character_counters)
    return sorted(list_of_character_counters, key=return_num_from_dict, reverse=True)