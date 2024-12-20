# An iterator for returning list elements
class ReverseIterator:
    def __init__(self, lst):
        self.lst = lst
        self.index = len(lst)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.lst[self.index]


my_list = [1, 2, 3, 4, 5]
for item in ReverseIterator(my_list):
    print(item)

print("-" * 100)

# An iterator that returns all even numbers in the range 0 to N
class EvenIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        result = self.current
        self.current += 2
        return result


for num in EvenIterator(10):
    print(num)
