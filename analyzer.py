def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    return len(text)

def find_most_common_word(text):
    counter = 0
    words = text.split()
    most_common = ''
    for word in words:
        curr_frequency = words.count(word)
        if(curr_frequency> counter):
            counter = curr_frequency
            most_common = word
    return most_common