def unique_in_order(sequence):
    result = []
    for i in sequence:
        if len(result) == 0 or i != result[-1]:
            result.append(i)
    return result