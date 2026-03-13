# ===========================================================================
# TODO: Travel Weather Planner
# ===========================================================================
#
# DESCRIPTION:
# For this exercise, you will use conditional statements to determine whether
# commuting is possible based on the weather, the distance to travel, and the
# availability of a vehicle.
#
# OBJECTIVE:
# Fulfill the requirements below and get all the tests to pass to complete
# the exercise.
#
# ===========================================================================
# REQUIREMENTS:
# ===========================================================================
#
# 1. CREATE THE FOLLOWING VARIABLES:
#    - distance_mi: a number representing the distance to travel in miles
#    - is_raining: a boolean representing if it's currently raining
#    - has_bike: a boolean representing if the user has a bicycle
#    - has_car: a boolean representing if the user has a car
#    - has_ride_share_app: a boolean representing if the user has a ride-share app
#
# 2. USE CONDITIONAL LOGIC:
#    - Use if, elif, and else statements to evaluate distance categories
#    - Evaluate the distance categories in ascending order
#    - Use boolean operators (and, or, not) in your conditions
#
# 3. IMPLEMENT THE FOLLOWING LOGIC:
#
#    a) If distance_mi is a falsy value:
#       → Print False
#
#    b) If the distance is less than or equal to 1 mile:
#       → Print True ONLY if it is NOT raining
#       → Otherwise, print False
#
#    c) If the distance is greater than 1 mile AND less than or equal to 6 miles:
#       → Print True ONLY if the person has a bike AND it is NOT raining
#       → Otherwise, print False
#
#    d) If the distance is greater than 6 miles:
#       → Print True if the person has a car OR has a ride-share app
#       → Otherwise, print False
#
# ===========================================================================
# TESTS TO PASS:
# ===========================================================================
#
# ✓ Passed: 1. You should have a variable named distance_mi.
# ✓ Passed: 2. You should assign a number to your distance_mi variable.
# ✓ Passed: 3. You should have a variable named is_raining.
# ✓ Passed: 4. You should assign a boolean to your is_raining variable.
# ✓ Passed: 5. You should have a variable named has_bike.
# ✓ Passed: 6. You should assign a boolean to your has_bike variable.
# ✓ Passed: 7. You should have a variable named has_car.
# ✓ Passed: 8. You should assign a boolean to your has_car variable.
# ✓ Passed: 9. You should have a variable named has_ride_share_app.
# ✓ Passed: 10. You should assign a boolean to your has_ride_share_app variable.
# ✗ Failed: 11. You should use at least one if statement.
# ✗ Failed: 12. You should use at least one elif branch in your program.
# ✗ Failed: 13. You should use at least one boolean operator (and, or, or not).
# ✗ Failed: 14. You should use the print() function to display the result.
# ✗ Failed: 15. When distance_mi is a falsy value, the program should print False.
# ✗ Failed: 16. When distance is 1 mile or less and NOT raining → print True.
# ✗ Failed: 17. When distance is 1 mile or less and IS raining → print False.
# ✗ Failed: 18. When distance is 1-6 miles, raining, no bike → print False.
# ✗ Failed: 19. When distance is 1-6 miles, not raining, no bike → print False.
# ✗ Failed: 20. When distance is 1-6 miles, has bike, not raining → print True.
# ✗ Failed: 21. When distance > 6 miles and has ride-share app → print True.
# ✗ Failed: 22. When distance > 6 miles and has car → print True.
# ✗ Failed: 23. When distance > 6 miles, no car, no ride-share → print False.
#
# ===========================================================================
# YOUR CODE BELOW:
# ===========================================================================

distance_mi = 7
is_raining = False
has_bike = True
has_car = False
has_ride_share_app = True

if not distance_mi:
    print(False)
elif distance_mi <= 1:
    if not is_raining:
        print(True)
    else:
        print(False)
elif distance_mi <= 6:
    if has_bike and not is_raining:
        print(True)
    else:
        print(False)
else:
    if has_car or has_ride_share_app:
        print(True)
    else:
        print(False)
