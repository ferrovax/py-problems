# 8.2
# Robot starts at upper left of grid, tries to find a path to bottom right
# Robot only moves right or down
# False spaces in the grid are off limits (obstacles)

def findPath(grid):
    if grid == None or len(grid) == 0:
        return None

    path, cache = [], set()

    if pathfinder(grid, len(grid) - 1, len(grid[0]) - 1, path, cache):
        return path

    return None

def pathfinder(grid, row, col, path, cache):
    if row < 0 or col < 0 or not grid[row][col]:
        return False

    pt = (row, col)

    if pt in cache:
        return False

    if (row == 0 and col == 0) or pathfinder(grid, row - 1, col, path, cache) or pathfinder(grid, row, col - 1, path, cache):
        path.append(pt)

        return True

    cache.add(pt)
    return False
