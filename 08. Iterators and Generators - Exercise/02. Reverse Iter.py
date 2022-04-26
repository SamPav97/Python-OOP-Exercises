class reverse_iter:
    def __init__(self, lst):
        self.lst = lst
        self.i = len(lst) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= 0:
            curent = self.i
            self.i -= 1
            return self.lst[curent]
        else:
            raise StopIteration()


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
