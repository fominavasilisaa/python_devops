field_map = [["."] * 3] * 2
print(field_map)
field_map[0][1] = "*"
print(field_map)

print()

def minefield(rows: int, cols: int, mines: list[tuple[int, int]]) -> list[list[str]]:
    field = []
    for _ in range(rows):
        row = ["."] * cols
        field.append(row)

    for r, c in mines:
        field[r][c] = "*"

    return field
print(minefield(2, 3, [(0, 1)]))
print(minefield(0, 3, []))
minefield(2, 0, [])