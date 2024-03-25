# class Worker:
#     def __init__(self, n, s, b=None):
#         self.lname = n
#         self.ssn = s
#         self.boss = b


# w = Worker("white", 123)
# w2 = Worker("John", 1234, w)

class Example:
    def __init__(self, x):
        self.x = x

    def foo(self, y):
        x = self.bar(y+1)
        return x

    def bar(self, y):
        self.x = y-1
        return self.x


a = Example(3)

print(a.foo(4))
