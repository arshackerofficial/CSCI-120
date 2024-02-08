# # Insetion Sort
# def insertionSort(arr):
#     n = len(arr)
#     if n <= 1: return arr
#     for i in range(1, n):
#         key = arr[i]
#         j = i-1
#         while j >= 0 and key < arr[j]:
#             arr[j+1] = arr[j]
#             j -= 1
#         arr[j+1] = key
#     return arr
        
# arr = [0,2,3,1,9]
# print(insertionSort(arr))

# Seletion Sort

# def seletionSort(array, ascending=True):
#     size = len(array)
#     for i in range(size):
#         min_index = i
#         for j in range(i+1, size):
#             if array[j] < array[min_index]: 
#                 min_index = j
#         array[i], array[min_index]  = array[min_index], array[i]
    
#     if not ascending:
#         array = array[::-1]
    
#     return array
        
# arr = [2,3,5,4,1]
# size = len(arr)
# print(seletionSort(arr, False))


# return middle half of the string

# def middle(text):
#     third = len(text) // 3
#     return text[third: len(text)-third]

# print(middle("abcabc"))


# check if its reverse of the string


# def indenticalStrings(s1, s2):
#     # reverse = ""
#     # for i in range(len(s1)):
#     #     reverse += s1[len(s1) -1 -i]
#     # return s2 == reverse
#     return s1 == s2[::-1]
    
# text1 = "abc"
# text2 = "cba"
# print(indenticalStrings(text1, text2))
