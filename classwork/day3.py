# try:
#     result = input("Number: ")
#     number = float(result)
#     print(f"Next number is {number+1}")
# except:
#     print("This is not a number")


# def first(x):
#     print("Starting first.")
#     try:
#         second(x)
#     except:
#         print("Caught at first")
#     print("Ending FIrst")
    
# def second(x):
#     print("Starting second.")
#     try:
#         third(x)
#     except  Exception as error:
#         print("Caught at second", type(error).__name__)
#     print("Ending second")
    
# def third(x):
#     print("Starting third.")
#     assert x<1
#     print("Ending third")
    
# first(2)

# ---------------------------------------------------------------------------------------------------------------------------------

# Remove Duplicate Function

# Version 1

# s = [1,1,4,7,2,10,1,2,7,8]
# s.sort()
# i=0
# while i<len(s):
#     try:
#         if(s[i] == s[i+1]):
#             s.pop(i)
#         else:
#             i+=1
#     except:
#         i=len(s)
    
# print(s)


# Version 2

# s = [1,1,4,7,2,10,1,2,7,8]
# i=0
# while i<len(s):    
#     if(s.count(s[i]) != 1):
#         s.remove(s[i])
#     i+=1
    
# print(s)

# --------------------------------------------------------------------------------------------------------------------------------------------

# Remove Singlets

# s = [1,4,4,7,2,10,1,2,7,8]
# i=0
# while i<len(s):    
#     if(s.count(s[i]) == 1):
#         s.remove(s[i])
#     i+=1
    
# print(s)

# ---------------------------------------------------------------------------------------------------------------------------------------------

# cities, city = [], ""
# while(city != "exit"):
#     city = input("Enter a name of city: ").lower()
#     if not city in cities and city != "exit": cities.append(city)
#     if "o" in city:
#         print(city.replace("o", "").capitalize())


# -----------------------------------------------------------------------------------------------------------------------------------------------


# Sorting Function, Bubble Sort, Maybe. Out of Syllabus

# s = [9,1,4,4,7,2,10,1,2,7,8]

# for i in range(len(s)):
#     x = i
#     while x >= 0 and i != (len(s)-1): 
#         if s[x] > s[x+1]: s[x], s[x+1] = s[x+1], s[x]
#         x-=1

# print(s)



# QuickSort

# import random

# def quick_sort(array):
#     if(len(array) <= 1): 
#         return array
#     pivot_index = random.randrange(0,len(array)-1,1)
#     pivot = array[pivot_index]
#     array.remove(pivot)
#     left = []
#     right = []
#     for element in array:
#         if(element > pivot):
#             right.append(element)
#         else:
#             left.append(element)
#     print(left,right)

#     return quick_sort(left) + [pivot] + quick_sort(right)

# print(quick_sort([6,5,6,5,3,8,3,9,2]))


# Merge Sort

# def merge_sort(array):
#     if(len(array) <= 1): return array
    
#     center = len(array) // 2
    
#     left = merge_sort(array[:center])
#     right = merge_sort(array[center:])
    
#     merged_array = []
    
    
#     left_index = 0
#     right_index = 0    
#     while left_index < len(left) and  right_index < len(right):
#         if(left[left_index] < right[right_index]):
#             merged_array.append(left[left_index])
#             left_index+=1
#         else:
#             merged_array.append(right[right_index])
#             right_index += 1
            
#     merged_array += left[left_index:]
#     merged_array += right[right_index:]
    
#     print(merged_array)
#     return merged_array

# print(merge_sort([6,5,6,5,3,8,3,9,2]))

# ----------------------------------------------------------------------------------------------------------------------------------------------