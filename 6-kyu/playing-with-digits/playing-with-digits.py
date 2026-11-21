def dig_pow(n, p):
    total = 0
    for i in str(n):
        total = total + int(i) ** p
        p += 1
    if total % n == 0:
        return total // n
    else:
        return -1