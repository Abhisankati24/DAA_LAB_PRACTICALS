5
def merge(arr, left, mid, right):
    leftSubArray = arr[left:mid + 1]
    rightSubArray = arr[mid + 1:right + 1]
    i = 0
    j = 0
    k = left
    while i < len(leftSubArray) and j < len(rightSubArray):
        if leftSubArray[i] <= rightSubArray[j]:
            arr[k] = leftSubArray[i]
            i += 1
        else:
            arr[k] = rightSubArray[j]
            j += 1
        k += 1
    while i < len(leftSubArray):
        arr[k] = leftSubArray[i]
        i += 1
        k += 1
    while j < len(rightSubArray):
        arr[k] = rightSubArray[j]
        j += 1
        k += 1
def mergeSort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)
        merge(arr, left, mid, right)
arr = list(map(int, input("Enter the numbers separated by spaces: ").split()))
mergeSort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)