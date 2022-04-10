from math import floor


class Integer:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if isinstance(float_value, float):
            return cls(floor(float_value))
        else:
            return f"value is not a float"

    @classmethod
    def from_string(cls, value):
        if not isinstance(value, str):
            return "wrong type"

        try:
            return cls(int(value))
        except ValueError:
            return "wrong type"

    @classmethod
    def from_roman(cls, _value):
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
                 'CD': 400, 'CM': 900}
        i = 0
        num = 0
        while i < len(_value):
            if i + 1 < len(_value) and _value[i:i + 2] in roman:
                num += roman[_value[i:i + 2]]
                i += 2
            else:
                # print(i)
                num += roman[_value[i]]
                i += 1
        return cls(num)


first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string("2.6"))
