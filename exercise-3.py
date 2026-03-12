# ============================================================================
# TODO: Simple calculator

# Write a calc function. It takes three arguments.
# The default value for the third argument is "multiply".
# The first two arguments are values that are to be combined using the operation requested by the third argument,
# a string that is one of the following `add`, `subtract`, `multiply`, `divide`, `modulo`, `int_divide` (for integer division) and `power`.
# The function returns the result.
# ============================================================================




def calc(first, second, operand="multiply"):
    # match only works for python versions 3.10 and above
    match operand:
        case "add":
            return first + second
        case "subtrach":
            return first - second
        case "multiply":
            return first * second
        case "divide":
            return first / second
        case "modulo":
            return first % second
        case "int_divide":
            return first // second
        case "power":
            return first * second
        

print(calc(4,2,"divide"))
