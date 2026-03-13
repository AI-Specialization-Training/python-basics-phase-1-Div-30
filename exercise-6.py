# ============================================================================
# TODO: Number Pattern Generator

# 1. Define a function named number_pattern that takes a single parameter n (representing a positive integer).
# 2. number_pattern should use a for loop.
# 3. number_pattern(n) should return a string with all the integers starting from 1 up to n (included) separated by a space. 
# For example, number_pattern(4) should return the string 1 2 3 4.
# 4. If the argument passed to the function is not an integer value, the function should return Argument must be an integer value.
# 5. If the argument passed to the function is less than 1, the function should return Argument must be an integer greater than 0.

# >>>>>>>>>>>>>
      # 1. number_pattern(12) should return the string 1 2 3 4 5 6 7 8 9 10 11 12.
    
      # 2. number_pattern(4) should return 1 2 3 4

      # 3. number_pattern should return Argument must be an integer value. when passed a value that is not an integer.

      # 4. number_pattern should return Argument must be an integer greater than 0. when passed a non-positive integer.

# >>>>>>>>>>>>>
# ============================================================================
def number_pattern(n):
        if type(n) != int:
            return "Argument must be an integer value"
        if n < 1:
            return "Argument must be an integer greater than 0"

        result = ""
        for i in range(1, n + 1):
            if i == n:
                result += str(i)
            else:
                result += str(i) + " "
        return result

print(number_pattern(5))