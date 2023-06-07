def calc(n1: int, n2: int, op):
    if not isinstance(n1, int) or not isinstance(n2, int):
        return "Error"
    if op == "+":
        return n1 + n2
    if op == "-":
        return n1 - n2
    if op == "*":
        return n1 * n2
    if op == "/":
        return n1 / n2
    else:
        return "Error"
