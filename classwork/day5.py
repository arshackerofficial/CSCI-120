# Coding all Day


# sum of list

# def sumlist(items):
#     sum = 0
#     for item in items:
#         sum+=item
#     return sum

# print(sumlist([1,2,-8]))




# count how many items have same first and last word

# def matchWords(words):
#     output = []
#     for word in words:
#         if word[0] == word[-1]:
#             output.append(word)
#     return len(output)

# print(matchWords(["abc", "xyz", "aba", "1221"]))




# find words in string which are greater then a number

# def longWords(n, string):
#     words = string.split(" ")
#     output = []

    # output = [word for word in words if len(word) > n]
#     for word in words:
#         if len(word) > n:
#             output.append(word)
#     return output

# print(longWords(3, "the quick brown fox jumps over the lazy dog"))




# find sums of 2 numbers in array given which adds up to target

# def twoSum(nums, target):
#     sums = {}
    
#     for i in range(len(nums)):
#         num = nums[i]
#         complement = target - num
#         if complement in sums:
#             return [sums[complement], i]
#         sums[num] = i
        
# print(twoSum([1,2,3],3))

# def twoSum(nums, target):
#     sums = {}
    
#     for i in range(len(nums)):
#         num = nums[i]
#         complement = target - num
#         if complement in nums:
#             return [nums.index(complement), i].sort()
#         # sums[num] = i
        
# print(twoSum([1,2,3],3))




# Check if list contains prime numbers

# def is_prime(n):
#     for num in n:
#         if num <= 1:
#                 return False
#         for i in range(2, num):
#             if num % i == 0:
#                 return False
#     return True
    
# print(is_prime([2,3,7,5]))