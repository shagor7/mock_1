# This program generates a final number
# The final number will be used to reveal the Caesar Cipher shift key

# Starting value of result
result = 0

# Counter starts from 1
counter = 1

# Loop will continue until counter reaches 50
while counter <= 50:

    # If counter is divisible by 9
    if counter % 9 == 0:
        # Subtract the counter value from result
        result -= counter

        # FIXED:
        # In the question, this line was incorrect:
        # counter !- 2
        #
        # That is not valid Python syntax.
        # We use counter += 2 to increase the counter by 2.
        counter += 2

        # Skip the rest of the loop and go to the next iteration
        continue

    # Add the current counter value to result
    result += counter

    # Show the current counter and updated result
    print(f"Adding {counter} to the result: {result}")

    # FIXED:
    # In the question, this line was:
    # counter -= 1
    #
    # That was wrong because it decreases the counter.
    # Since the loop condition is counter <= 50,
    # decreasing the counter can cause an infinite loop.
    #
    # Correct version:
    # Increase counter by 1 so the loop can move forward and stop at 50.
    counter += 1

    # If counter is divisible by 17
    if counter % 17 == 0:
        # Skip the rest of the loop
        continue

# Divide the final result by 10 and convert it to an integer
# This reveals the shift key
shift = int(result / 10)

# Print the final shift key
print("\nThe final generated number is:", shift)

# the answer of the 1.2 b is 87