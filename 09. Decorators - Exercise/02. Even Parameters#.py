def even_parameters(function):
    def wrapper(*args):
        for num in args:
            try:
                if num % 2 != 0:
                    return "Please use only even numbers!"
            except:
                # this is a bad exception.
                return "Please use only even numbers!"
        return function(*args)

    return wrapper


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result

print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))

