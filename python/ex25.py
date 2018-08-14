def break_words(stuff):
    """Break up words for us"""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """sorts the words"""
    return sorted(words)

def print_first_word(words):
    """prints the first word after popping it up"""
    words = words.pop(0)
    print word

def print_last_word(words):
    """print the last word after popping it off"""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """takes infull sentence nd returns sorted wordss"""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """the first and last words of the sentence"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
        """sorts the words and then prints the first and last"""
        words = sort_sentence(sentence)
        print_first_word(word)
        print_last_word(words)
