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

# Solution
def data_type_conversion(a, b):
    try:
        if b == "float":
            return float(a)
        elif b == "str":
            return str(a)
        elif b == "int":
            return int(a)
        else:
            return "The data types must be float, str, or int"
    except ValueError as error:
        return f"Invalid data type {error}"
print(data_type_conversion(1, "str"))

