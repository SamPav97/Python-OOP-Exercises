def genrange(strt, end):
    while strt <= end:
        yield strt
        strt += 1

print(list(genrange(1, 10)))