def liner_search(key, arr):
    for i in range(1, len(arr)+1):
        if arr[-i] == key:
            return len(arr) - i
    return -1


# print(liner_search(44, [1, 2, 3, 4, 22, 55, 44]))


def binary_search(key, arr):
    left = 0
    right = len(arr)-1

    while left <= right:
        middle = (left + right) // 2
        if arr[middle] == key:
            return middle
        elif arr[middle] < key:
            left = middle + 1
        else:
            right = middle - 1

    return -1


# def binary_search(key, arr):

#     left = 0
#     right = len(arr)-1

#     while left <= right:
#         middle = (left + right) // 2
#         if arr[middle] == key:
#             return middle
#         elif arr[middle] < key:
#             left = middle + 1
#         else:
#             right = middle - 1

#     return -1


def binary_search(key, arr, i=0):
    if arr[0] == key:
        return i
    if key > arr[-1] or key < arr[0]:
        return -1
    ans = -1
    middle = len(arr) // 2
    if arr[middle] == key:
        return middle+i
    elif arr[middle] < key:
        ans = binary_search(key, arr[middle:], middle+i)
    else:
        ans = binary_search(key, arr[:middle], middle-i)
    return ans


def rotations(arr):
    current_rotations = 0
    if len(arr) == 0:
        return current_rotations
    if arr[0] > arr[-1]:
        arr.pop(0)
        current_rotations = 1 + rotations(arr)
    else:
        return -1
    return current_rotations


def rotated_binry(key, arr):
    rotation_point = rotations(arr[:])
    if rotation_point != -1:
        ans = max(binary_search(key, arr[rotation_point+1:], rotation_point+1),
                  binary_search(key, arr[:rotation_point+1], rotation_point+1))
    else:
        ans = binary_search(key, arr[:])
    return ans


print(binary_search(8, [6, 7, 8]))
print(binary_search(8, [1, 2, 3, 4, 5]))
print(rotated_binry(5, [6, 7, 8, 1, 2, 3, 4, 5]))
