def cap_first_letter(word):
    return word[0].upper() + word[1:]

def sentence_syntax(text):
    return cap_first_letter(text) + '.'