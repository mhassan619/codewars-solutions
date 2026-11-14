def sort_array(source_array):
    odd = []
    for i in source_array:
        if i % 2 != 0:
            odd.append(i)
    odd.sort()
    k = 0
    for i in range(0,len(source_array)):
        if source_array[i] % 2 != 0:
            source_array[i] = odd[k]
            k += 1
    return source_array