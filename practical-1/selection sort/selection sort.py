def selectionSort(arr):
    n = len(arr)

    for i in range(n - 1):
        minIndex = i

        for j in range(i + 1, n):
            if arr[j] < arr[minIndex]:
                minIndex = j

        arr[i], arr[minIndex] = arr[minIndex], arr[i]23
arr = list(map(int, input("Enter the numbers separated by spaces: ").split()))
selectionSort(arr)
print("Sorted Array:", arr)