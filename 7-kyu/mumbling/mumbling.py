def accum(st):
    result = ""
    k = 1
    for i in st:
        for j in range(1,k + 1,1):
            if j == 1:
                result = result + f"{i.upper()}"
            else:
                result = result + f"{i.lower()}"
        result = result + "-"
        k = k + 1
    return result[:-1]