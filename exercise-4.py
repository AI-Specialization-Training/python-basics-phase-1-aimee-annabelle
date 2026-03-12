# ============================================================================
# TODO: Data Type Conversion

#Create a function called data_type_conversion.
# It takes two parameters, the value and the name of the data type requested, one of float, str, or int.
# Return the converted value.
#Error handling: The function might be called with a bad parameter.
# For example, the caller might try to convert the string "nonsense" to a float.
# Catch the error that occurs in this case. If this error occurs,
# return the string You can't convert {value} into a {type}., so again you use a formatted string.

# ============================================================================

def data_type_conversion(value, converter):
    result = None
    match converter:
        case "float":
            try:
                result = float(value)
            except ValueError as e:
                return value
        case "str":
            try:
                result = str(value)
            except ValueError as e:
                return value
        case "int":
            try:
                result = int(value)
            except ValueError as e:
                return value
        case _:
            return value
    return result


print(data_type_conversion(1,"float"))