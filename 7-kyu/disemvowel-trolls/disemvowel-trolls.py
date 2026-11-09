def disemvowel(string_):
    vowels = ['a','i','o','e','u','A','E','I','O','U']
    for i in string_:
        if i in vowels:
            string_ = string_.replace(i,"")
    return string_