def second_highest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort(reverse=True)
    return unique_numbers[1] if len(unique_numbers) > 1 else None

numbers = [10, 20, 4, 45, 99, 99, 5]
print("Second highest number:", second_highest(numbers))