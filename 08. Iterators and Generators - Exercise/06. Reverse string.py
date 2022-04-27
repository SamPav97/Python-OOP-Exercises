def reverse_text(param):
    i = len(param) - 1
    while i >= 0:
        yield param[i]
        i -= 1


for char in reverse_text("step"):
    print(char, end='')
