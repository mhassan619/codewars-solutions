def smash(words):
    result = ""
    for i in words:
        result += i
        result  = result + " "
    return result[:-1]
    