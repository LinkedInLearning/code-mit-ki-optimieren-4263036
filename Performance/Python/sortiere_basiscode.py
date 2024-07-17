def sort_numbers(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers

numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sort_numbers(numbers)
print(sorted_numbers)