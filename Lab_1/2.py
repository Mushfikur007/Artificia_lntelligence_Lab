def smallest_number(numbers):

    smallest = numbers[0]

    for num in numbers:
        if num < smallest:
            smallest = num

    return smallest

numbers = [5, 2, 9, 1, 7, 3]
smallest_number = smallest_number(numbers)

print(f"The smallest number is: {smallest_number}")