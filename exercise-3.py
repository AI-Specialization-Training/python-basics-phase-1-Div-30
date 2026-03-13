# ============================================================================
# TODO: Simple calculator 

# Write a calc function. It takes three arguments. 
# The default value for the third argument is "multiply". 
# The first two arguments are values that are to be combined using the operation requested by the third argument, 
# a string that is one of the following `add`, `subtract`, `multiply`, `divide`, `modulo`, `int_divide` (for integer division) and `power`. 
# The function returns the result.
# ============================================================================

def calc (a, b, operation = "multiply"):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b
    elif operation == "modulo":
        return a % b
    elif operation == "int_divide":
        return a // b
    elif operation == "power":
        return a ** b
    else:
        return "Invalid operation"

