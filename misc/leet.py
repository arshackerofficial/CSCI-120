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



def num_perfect_squares(n): 
    if n <= 0: return 0
    perfect_squares = [i * i for i in range(1, int(n ** 0.5) + 1)]
    # count = float('inf')
    count = 0
    for square in perfect_squares:
        if square == n: return 1
        elif square < n: count = num_perfect_squares()
    return count


print(num_perfect_squares(44))