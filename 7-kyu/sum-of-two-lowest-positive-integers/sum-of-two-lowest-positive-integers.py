def sum_two_smallest_numbers(numbers):
    sum = 0
    for i in range(0,2):
        minimum = min(numbers)
        sum += minimum
        numbers.remove(minimum)
    return sum