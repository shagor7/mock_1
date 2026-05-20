import random

# Start with result = 0
result = 0

# Start counter from 1
counter = 1

# Generate 5 random numbers between 1 and 10
numbers = [random.randint(1, 10) for _ in range(5)]

# Print the generated random numbers so we can see what the program is using
print("Generated numbers:", numbers)

# Run the loop while counter is less than 10
while counter < 10:

    # If counter is even
    if counter % 2 == 0:
        # Add one selected number multiplied by 10 to the result
        result += numbers[counter % len(numbers)] * 10

        # Print the current step and result
        print(f"Stop {counter}: {result}")

        # Increase counter by 1 before continuing
        counter += 1
        continue

    # If counter is odd, multiply result by one selected number
    result *= numbers[counter % len(numbers)]

    # Go through each number in the list
    for num in numbers:
        # If the number is less than 5
        if num < 5:
            # Add that number multiplied by counter to the result
            result += num * counter

            # Stop the loop after finding the first number less than 5
            break

    # IMPORTANT CHANGE:
    # In Question 1.1, this line was:
    # counter -= 1
    #
    # That was wrong because it decreases the counter.
    # Since the while loop condition is counter < 10,
    # decreasing the counter can make the loop run forever.
    #
    # Correct version:
    # We increase counter by 1 so the loop can move toward 10 and stop properly.
    counter += 1

# Print the final generated number
print("\nThe final generated number is:", result // 10)