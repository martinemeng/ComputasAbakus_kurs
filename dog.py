coordinates = [(0, 0)]
distances = [1, 1]

# nord, øst, sør, vest
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

for step in range(63):
    # beste retning basert på hvor i sekvensen vi er
    direction = directions[step % 4]
    
    # neste distanse 
    if step >= 2:
        next_distance = distances[-1] + distances[-2]
        distances.append(next_distance)
    else:
        next_distance = distances[step]
    
    # forrige posisjon
    last_x, last_y = coordinates[-1]
    
    # nye koordinater
    new_x = last_x + direction[0] * next_distance
    new_y = last_y + direction[1] * next_distance
    
    # legger til nye koordinater
    coordinates.append((new_x, new_y))

print(coordinates)