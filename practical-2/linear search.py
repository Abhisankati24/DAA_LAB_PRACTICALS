def linearSearch(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1
arr = list(map(int, input("Enter the elements separated by spaces: ").split()))
key = int(input("Enter the element to search: "))
result = linearSearch(arr, key)
if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found.")