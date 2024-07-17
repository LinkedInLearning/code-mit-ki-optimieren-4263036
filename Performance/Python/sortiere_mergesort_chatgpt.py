def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    
    # Split the list into two halves
    middle = len(numbers) // 2
    left_half = numbers[:middle]
    right_half = numbers[middle:]
    
    # Recursively sort each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    sorted_list = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_list.append(left[left_index])
            left_index += 1
        else:
            sorted_list.append(right[right_index])
            right_index += 1
    
    # Append remaining elements
    sorted_list.extend(left[left_index:])
    sorted_list.extend(right[right_index:])
    
    return sorted_list

numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = merge_sort(numbers)
print(sorted_numbers)
