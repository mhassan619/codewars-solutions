def binary_array_to_number(arr):
    binary_string = "".join(str(b) for b in arr)
    decimal_val = int(binary_string,2)
    return decimal_val