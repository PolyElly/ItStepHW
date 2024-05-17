def division(a: float, b: float):
    if type(a) == str or type(b) == str:
        return TypeError
    if a == 0 or b == 0:
        return ZeroDivisionError
    return a / b