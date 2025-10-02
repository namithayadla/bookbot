def num_of_words(text):
    print("----------- Word Count ----------")
    split_words = text.split()
    count = len(split_words)
    message = f"Found {count} total words"
    return message

def count_chars(text):
    chars_dict = {}
    text = text.lower()
    for char in text:
        if char in chars_dict:
            chars_dict[char] += 1
        else: 
            chars_dict[char] = 1
    print("--------- Character Count -------")
    return chars_dict

def sort_on(items):
    return items["nums"]