# def sumSeries(n):
#     if n <= 1:
#         return n

#     return n + sumSeries(n-1)


# print(sumSeries(10))

# def find_avg(arr, n):
#     if len(arr) == 1:
#         return arr[0]

#     return (arr[0] + find_avg(arr[1:], 1))/n


# print(find_avg([1, 3, 5, 7], 4))


# def printT(a):
#     if len(a) == 1:
#         print(a)
#         return
#     printT([a[x-1]+a[x] for x in range(1, len(a))])
#     print(a)


# printT([1, 2, 3, 4, 5])

# def product(x, y):
#     if y == 1 or x == 1:
#         return max(y, x)

#     return x + product(x, y-1)


# print(product(6, 2))


# def printseq(n, k, prefix=[]):

#     if k == 0:
#         print(prefix)
#         return

#     start = 1 if not prefix else prefix[-1] + 1

#     for i in range(start, n + 1):
#         printseq(n, k - 1, prefix + [i])


# n = 3
# k = 2
# printseq(n, k)


# def prints(n):
#     if n == 1:
#         print("*")
#         return
#     print("*", end="")
#     prints(n-1)


# def triangle(n):
#     if n == 0:
#         return
#     triangle(n-1)
#     prints(n)


# triangle(3)


# def triange(n, i=""):
#     if n == 0:
#         return
#     i += "*"
#     print(i)
#     triange(n-1, i)

# triange(3)
