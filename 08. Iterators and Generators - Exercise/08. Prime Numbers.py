def get_primes(lst):
    for num in lst:
        if num == 0 or num == 1 or num < 0:
            continue
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))