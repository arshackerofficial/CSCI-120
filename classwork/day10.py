def insertionSort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr


arr = [0, 2, 3, 1, 9]
print(insertionSort(arr))


def insertionSort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    for i in range(1, n):
        key, j = push_down(arr, i)
        arr[j] = key
    return arr


def push_down(arr, i):
    key = arr[i]
    j = i-1
    while j >= 0 and key < arr[j]:
        swap(arr, j+1, j)
        j -= 1
    return key, j+1


def swap(arr, a, b):
    arr[a] = arr[b]


arr = [2, 1, 3, 0]
print(insertionSort(arr))


def seletionSort(array):
    size = len(array)
    for i in range(size):
        min_index = i
        for j in range(i+1, size):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

    return array
