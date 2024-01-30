# for i in range(1, 101):
#     print(i)

# seqn = [1,2,3,4,5]
# x = seqn[0]
# print(x)

# n = 10
# total = 0
# # for x in range(10):
# #     total = total + x
# x = 0
# while (x < n):
#     total = total + x
#     x += 1
    
# print(total)

# total = 0
# for i in range(5, 15, 2):
#     total += i
    
# print(total)



# total = 0
# x = 5

# while x < 15:
#     total += x
#     x += 2
    
# print(total)


# stations = ["main", "metro", "waterfront", "central"]
# reversed= False
# x=0
# while x<(len(stations)):
#         print("next station is : " + stations[x])
#         if(x==(len(stations)-1)):
#             reversed = True
#         if reversed:
#             if(x==0):
#                 break
#             x -= 1
#         else:
#             x += 1

# n=0
# double = 2*len(stations)
# x = -5
# while n<double:
#     print("next station is : " + stations[n - (0 if n<len(stations) else x)])
#     print(n-len(stations))
#     n += 1
#     x +=1

stations, x, reversed = ["main", "metro", "waterfront", "central"], 0, False
while 0 <= x < len(stations): print("next station is : " + stations[x]); x += -1 if reversed else 1; reversed = True if x == len(stations) - 1 and not reversed else reversed