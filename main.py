# coordinates grid and trajectory

coordinates_row = []
coordinates_col = []
rhombus = []

d = 3  # always odd, minimum 3, dimension, number of cells

m = int((d-1)/2)
print("Distance from centre (0,0) to apex:", m)

# raws list
for row in range(-m, m+1):
    coordinates_row.extend([row] * (d))

print(coordinates_row)

# column list
for col in range(-m, m+1):
    for col in range(-m, m+1):
        coordinates_col.append(col)

print(coordinates_col)

# rows and columns together
coordinates = zip(coordinates_row, coordinates_col)
coordinates = list(coordinates)
print("Coordinates grid:", coordinates)

# start_index = coordinates.index((1, 2))
# print(start_index)

# The coordinates of the points on the hollow rhombus satisfies |x|+|y|==m (where m = n-1)
for row in range(-m, m+1):
    for col in range(-m, m+1):
        if abs(row) + abs(col) == m:
            rhombus.append((col, row))

print("Rhombus trajectory:", rhombus)
