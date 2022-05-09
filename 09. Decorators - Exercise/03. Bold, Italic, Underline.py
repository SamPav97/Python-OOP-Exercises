def make_bold(function):
    def wrapper(*name):
        return f"<b>{function(*name)}</b>"
    return wrapper


def make_italic(function):
    def wrapper(*name):
        return f"<i>{function(*name)}</i>"
    return wrapper


def make_underline(function):
    def wrapper(*name):
        return f"<u>{function(*name)}</u>"
    return wrapper


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"


print(greet_all("Peter", "George"))
