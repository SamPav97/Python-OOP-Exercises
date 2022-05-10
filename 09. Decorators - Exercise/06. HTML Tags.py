def tags(tag):
    def decorator(function):
        def wrapper(*args):
            res = function(*args)
            return f"<{tag}>{res}</{tag}>"
        return wrapper
    return decorator


@tags('p')
def join_strings(*args):
    return "".join(args)
print(join_strings("Hello", " you!"))
