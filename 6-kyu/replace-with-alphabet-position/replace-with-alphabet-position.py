def alphabet_position(text):
    result = ''
    for i in text:
        if i.isalpha():
            result = result + str(ord(i.lower()) - 96) + " "
    return result[:-1]