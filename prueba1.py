def calc(n1: int, n2: int, op):
    if not isinstance(n1, int) or not isinstance(n2, int):
        return "Error"
    match op:
        case "+":
            return n1 + n2
        case "-":
            return n1 - n2
        case "*":
            return n1 * n2
        case "/":
            return n1 / n2
        case _:
            return "Error"
