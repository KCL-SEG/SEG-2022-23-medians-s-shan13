"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]

        numbers.sort()
        length = len(numbers)
        if not length: print(0)
        mid = length//2
        if length %2==0:
            print(numbers[mid]+numbers[mid-1])/2
        else:
            print(numbers[mid])

    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)
