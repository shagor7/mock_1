def draw_pattern(rows=20, cols=33):
    """
    Draws a pattern with:
    - Top and bottom border rows of '#' characters
    - Inner rows with a repeating '*#@%' cycle,
      prefixed and suffixed with '#' border characters
    """
    symbols = ['*', '#', '@', '%']
    width = cols

    # Top border row
    print('#' * width)

    # Inner rows
    for row in range(rows - 2):
        line = '#'  # left border
        for col in range(width - 2):
            # Each row shifts the starting symbol by 1 (diagonal effect)
            line += symbols[(col + row) % 4]
        line += '#'  # right border
        print(line)

    # Bottom border row
    print('#' * width)


draw_pattern()