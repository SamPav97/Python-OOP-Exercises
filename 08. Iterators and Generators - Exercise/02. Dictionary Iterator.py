class dictionary_iter:
    def __init__(self, dic):
        self.dic = dict(reversed(list(dic.items())))

    def __iter__(self):
        return self

    def __next__(self):
        while self.dic:
            k_v = self.dic.popitem()
            return k_v
        else:
            raise StopIteration()


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
