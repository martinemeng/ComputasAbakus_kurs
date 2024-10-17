#start
coordinates = [(0, 0)]
distances = [1, 1]  # Fibonacci-like sequence starting with 1, 1

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

for step in range(63):
    # Determine the direction based on the step
    direction = directions[step % 4]
    
    # Calculate the next distance in the Fibonacci sequence
    if step >= 2:
        next_distance = distances[-1] + distances[-2]
        distances.append(next_distance)
    else:
        next_distance = distances[step]
    
    # Get the last position
    last_x, last_y = coordinates[-1]
    
    # Calculate the new coordinates
    new_x = last_x + direction[0] * next_distance
    new_y = last_y + direction[1] * next_distance
    
    # Append the new coordinates
    coordinates.append((new_x, new_y))

print(coordinates)