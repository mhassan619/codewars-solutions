def disemvowel(string_):
    vowels = 'aeiouAIEOU'
    return "".join(char for char in string_ if char not in vowels)