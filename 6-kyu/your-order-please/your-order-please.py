def order(sentence):
    if sentence == "":
        return ""
    else:
        words = sentence.split()
        result = [""] * len(words)
        for word in words:
            for char in word:
                if char.isdigit():
                    result[int(char) - 1] = word
        return " ".join(result)