def printer_error(s):
    error = 0
    for char in s:
        if char > 'm':
            error += 1
    return f"{error}/{len(s)}"