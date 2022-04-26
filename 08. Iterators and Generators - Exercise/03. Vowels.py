class vowels:
    def __init__(self, text):
        self.text = text
        self.i = 0
        self.end = len(text) - 1

    def __iter__(self):
        return self

    def __next__(self):
        while self.i <= self.end:
            current = self.i
            self.i += 1
            if self.text[current] in "AEIOUYaeiouy":
                return self.text[current]
        else:
            raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
