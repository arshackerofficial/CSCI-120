    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for x in range(len(nums)):
    #         for y in range(x+1,len(nums)):
    #             sum = nums[x] + nums[y]
    #             if sum == target:
    #                 return [x, y]

# strs = ["ddddddddddg","dgggggggggg"]

# full_list = []

# for i in range(len(strs)):
#     current_string = strs[i]
#     is_anagram = False
#     list_anagram = []
    
#     for j in range(i+1, len(strs)):
#         next_string = strs[j]
        
#         if len(next_string) == len(current_string):
#             is_anagram = True
#             for k in range(len(next_string)):
#                     if not(next_string[k] in current_string and current_string.count(next_string[k]) == next_string.count(next_string[k])):
#                         is_anagram = False
#             if is_anagram:
#                 if list_anagram:
#                     list_anagram.append(next_string)
#                     is_anagram = False
#                 else:
#                     list_anagram = [current_string, next_string]
#                     is_anagram = False
                    
#     if not list_anagram: list_anagram = [current_string]
#     if full_list:
#         add = True
#         for full_element in full_list:
#             first = list_anagram[0]
#             if first in full_element:
#                 add = False
#         if add: full_list.append(list_anagram)
                
#     else: full_list.append(list_anagram)
    
# print(full_list)

# nums = [3,2,4]
# target = 6
  
# for x in range(len(nums)):
#     for y in range(x+1,len(nums)):
#         sum = nums[x] + nums[y]
#         if sum == target:
#             print([x, y]) 

# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000


# numberDict = {
#     "i": 1,
#     "v": 5,
#     "x": 10,
#     "l": 50,
#     "c": 100,
#     "d": 500,
#     "m": 1000,
# }

# roman = "MCMXCIV".lower()

# num = 0
# for i in range(len(roman)):
#     romanInts = list(numberDict.keys())
#     this_index = romanInts.index(roman[i])
#     to_add = numberDict[roman[i]]
    
#     try: 
#         next_index = romanInts.index(roman[i+1]) 
#         if next_index and this_index < next_index:
#             to_add = numberDict[roman[i+1]] - numberDict[roman[i]]
#     except: pass  
    
#     if i != 0: 
#         if romanInts.index(roman[i-1]) < this_index:
#             to_add = 0
    
#     num += to_add
    
# print(num)

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# strs = ["flower","flow","flight"]

# output, prev_item = "", ""

# for item in strs:
#     for char in prev_item:
#         if char in item:
#             output += char
#     prev_item = item
# print(output)










# Example 1:

# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.
# Example 2:

# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.



# def num_perfect_squares(n): 
#     if n <= 0: return 0
#     perfect_squares = [i * i for i in range(1, int(n ** 0.5) + 1)]
#     # count = float('inf')
#     count = 0
#     for square in perfect_squares:
#         if square == n: return 1
#         elif square < n: count = num_perfect_squares()
#     return count


# print(num_perfect_squares(44))

# def reverseString(string):
#     if len(string) < 2:
#         return string
#     return string[-1] +  reverseString(string[:-1])

# print(reverseString("arsh preet"))

# def isPalandrome(string):
#     if len(string) < 2: return True
    
#     check = string[0] == string[-1]
    
#     if not check: return False
    
#     return check and isPalandrome(string[1:-1])

# print(isPalandrome("kanak"))

# def numToBinary(num):
#     if num < 2:  return 1
#     return num % 2 + numToBinary(num // 2)*10
    

# print(numToBinary(233))

# def sumNaturalNumbers(num):
#     if num < 2:  return 1
#     return num + sumNaturalNumbers(num-1)

# print(sumNaturalNumbers(100))



# def sumNaturalNumbers(num):
#     return (num * (num+1))//2

# print(sumNaturalNumbers(100))


# def binarySearch(sorted_list, num):
#     length = len(sorted_list)
#     mid_point = length//2
#     mid = sorted_list[mid_point]
    
#     # Base Cases
#     if num not in sorted_list: return "Number is not in list"
#     if length < 2: return 0
#     elif num == mid: return mid_point
    
#     # Recursion
#     if num > mid: return mid_point + binarySearch(sorted_list[mid_point:], num)
#     elif num < mid: return binarySearch(sorted_list[:mid_point], num)
    
# print(binarySearch([1,2,3,4,5], 5))





# # without memoization - 137.8 ms

# def fibonachiSeries(number):
#     if number == 0 or number == 1: return number
#     return fibonachiSeries(number-1)+fibonachiSeries(number-2)

# print(fibonachiSeries(11))


# # with memoization - 0.0 ms

# cache = {0:0, 1:1}
# def fibonachiSeries(number):
    
#     # Base Case
#     if number in cache:
#         return cache[number]
    
#     # Recursion
#     series = fibonachiSeries(number-1)+fibonachiSeries(number-2)
#     cache.update({number: series})
#     return series

# print(fibonachiSeries(30))



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
    
#     return merged_array

# print(merge_sort([6,5,6,5,3,8,3,9,2]))





# maximum sum of contiguious subarray of 3

# def sumMax(list):
#     maxsum = float("-inf")
#     sum_list = []
#     for i in range(2, len(list)):
#         item1, item2, item3 = list[i-2], list[i-1], list[i]
#         new_sum = item1 + item2 + item3
#         if new_sum > maxsum:
#             maxsum = new_sum
#             sum_list = [item1, item2, item3]
    
#     return sum_list

# print(sumMax([1,12,3,4,51]))



# IDK WTF IS THIS!!!!

# def smallestSubArraySum(list, sum):
#     size = float("inf")
    
#     i = 0
#     j = 0
    
#     currentSum = 0
#     while i < len(list):
#         currentSum += list[i]
#         while currentSum >= sum:
#             size = min(size, i-j+1)
#             currentSum -= list[j]
#             j+=1
#         i+=1
#     return size

# print(smallestSubArraySum([1,2,3,5], 5))




# def longestSubstring(string, k):
#     j = 0
#     maximum = float("-inf")
#     prevMax = float("-inf")
#     strr = ""
#     for x in range(len(string)):
#         i = x + 1
#         output = ""
#         length = 0
#         while i < len(string) and length < k:
#             if not (string[i-1] == string[i]): length += 1
#             output += string[i-1]
#             i+=1
#         prevMax = maximum
#         maximum = max(maximum, len(output))
#         if maximum > prevMax:
#             strr = output
#     return strr
        

# print(longestSubstring("taaahhttttb", 2))