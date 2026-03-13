# ============================================================================
# TODO: Use a For Loop with a Range 

#Create a function called repeat. 
# It takes two parameters, a string and a count, and returns a new string that is the old one repeated count times.
# ============================================================================

def repeat(value, count):
    result = ""
    for i in range(count):
        result += value
    return result

print(repeat("amen", 5))
