# Function to draw a single line (tick) of the ruler
def draw_line(tick_length, tick_label=''):
    """
    Draw one line with the given tick length (followed by an optional label).
    """
    # Create the tick mark with '-' repeated 'tick_length' times
    line = '-' * tick_length
    # If there's a label (like '0', '1', etc.), append it to the tick mark
    if tick_label:
        line += ' ' + tick_label
    # Print the tick mark (with or without the label)
    print(line)

# Function to recursively draw the intervals between major ticks
def draw_interval(center_length):
    """
    Draw tick interval based on a central tick length.
    """
    # Base case: If the tick length is 0, do nothing (end recursion)
    if center_length > 0:
        # Recursively draw the top ticks (ticks above the central tick)
        draw_interval(center_length - 1)
        # Draw the central tick (for this interval)
        draw_line(center_length)
        # Recursively draw the bottom ticks (ticks below the central tick)
        draw_interval(center_length - 1)

# Function to draw the entire ruler
def draw_ruler(num_inches, major_length):
    """
    Draw an English ruler with the given number of inches and major tick length.
    """
    # Draw the first major tick mark (for inch 0)
    draw_line(major_length, '0')
    # Loop through each inch, drawing the minor ticks and the major tick
    for j in range(1, 1 + num_inches):
        # Draw the minor ticks between this inch and the next
        draw_interval(major_length - 1)
        # Draw the major tick mark for this inch (with label)
        draw_line(major_length, str(j))

# Example usage: Draw a 2-inch ruler with major tick length of 4
draw_ruler(5, 4)