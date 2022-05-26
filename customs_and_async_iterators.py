class OddIterator:
    def __init__(self, max_num):
        self.max_num = max_num
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num > self.max_num:
            raise StopIteration
        else:
            self.num += 2
            return self.num - 2


o1 = OddIterator(10)
print(o1.__next__())
print(list(o1))
