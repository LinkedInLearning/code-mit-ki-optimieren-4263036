def sort_numbers(numbers):
  if len(numbers) <= 1:
    return numbers
  for i in range(1, len(numbers)):
    current_item = numbers[i]
    j = i - 1
    while j >= 0 and numbers[j] > current_item:
      numbers[j + 1] = numbers[j]
      j -= 1
    numbers[j + 1] = current_item
  return numbers