
class Calculator:

    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        p = 1
        for i in args:
            p *= i
        return p

    @staticmethod
    def divide(*args):
        p = args[0]
        for ind in range(1, len(args)):
            p /= args[ind]
        return p

    @staticmethod
    def subtract(*args):
        p = args[0]
        for ind in range(1, len(args)):
            p -= args[ind]
        return p


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
