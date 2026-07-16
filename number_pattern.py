"Lab Build a Number Pattern Generator"

def number_pattern(n):
    if type(n) is not int:
        return "Argument must be an integer value."
    if n < 1:
        return "Argument must be an integer greater than 0."

    pattern = ""

    for i in range(1, n + 1): 
        pattern += str(i) + " "
    return pattern.strip()

