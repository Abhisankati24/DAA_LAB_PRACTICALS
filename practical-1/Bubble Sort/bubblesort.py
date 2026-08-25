# Bubble Sort

n = int(input("Enter the number of elements: "))

arr = []
for i in range(n):
    arr.append(int(input(f"Enter element {i + 1}: ")))

# Bubble Sort
for i in range(n - 1):
    swapped = False
    for j in range(n - 1 - i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = True
    if not swapped:
        break

print("Sorted array:",arr)