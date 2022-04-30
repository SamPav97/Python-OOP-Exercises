
def solution():

    def integers():
        x = 1
        while True:
            current = x
            x += 1
            yield current

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        lst = []
        for _ in range(n):
            lst.append(next(seq))
        return lst

    return (take, halves, integers)


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
