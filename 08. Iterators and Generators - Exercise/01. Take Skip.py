class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.count > 0:
            now = self.current
            self.current += self.step
            self.count -= 1
            return now
        else:
            raise StopIteration()


numbers = take_skip(10, 5)
for number in numbers:
    print(number)

