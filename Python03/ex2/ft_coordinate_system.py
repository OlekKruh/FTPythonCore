import math

pos1 = (10, 20, 5)
distance1 = math.sqrt((pos1[0] - 0)**2 + (pos1[1] - 0)**2 + (pos1[2] - 0)**2)

print("=== Game Coordinate System ===")
print(f"Position created: {pos1}")
print(f"Distance between (0, 0, 0) and {pos1}: {distance1:.2f}\n")

# ===============
coord_str = "3,4,0"
parts = coord_str.split(',')
pos2 = (int(parts[0]), int(parts[1]), int(parts[2]))
distance2 = math.sqrt((pos1[0] - 0)**2 + (pos1[1] - 0)**2 + (pos1[2] - 0)**2)

print(f'Parsing coordinates: "{coord_str}"')
print(f"Parsed position: {pos2}")
print(f"Distance between (0, 0, 0) and {pos2}: {distance2}\n")

# ===============
invalid_str = "abc, def, ghi"

print(f'Parsing invalid coordinates: "{invalid_str}"')

try:
    parts_invalid = invalid_str.split(',')
    val = int(parts_invalid[0])
except ValueError as e:
    print(f"Error parsing coordinates: {e}")
    print(f"Error details - Type: {type(e).__name__}, Args: {e.args}\n")

x, y, z = pos2

print("Unpacking demonstration:")
print(f"Player at x={x}, y={y}, z={z}")
print(f"Coordinates: X={x}, Y={y}, Z={z}")
