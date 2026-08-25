def partition(numbers, start, end):
    pivot = numbers[end]
    index = start - 1

    for current in range(start, end):
        if numbers[current] <= pivot:
            index += 1
            numbers[index], numbers[current] = numbers[current], numbers[index]

    numbers[index + 1], numbers[end] = numbers[end], numbers[index + 1]
    return index + 1


def quick_sort(numbers, start, end):
    if start < end:
        p = partition(numbers, start, end)
        quick_sort(numbers, start, p - 1)
        quick_sort(numbers, p + 1, end)


# User Input
numbers = list(map(int, input("Enter the elements separated by spaces: ").split()))

quick_sort(numbers, 0, len(numbers) - 1)

print("Sorted Array:", numbers)