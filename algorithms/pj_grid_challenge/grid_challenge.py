def gridChallenge(grid):
    # Write your code here
    grid = [sorted(row) for row in grid]
    t = tuple(zip(*grid))
    if all([row[i] <= row[i + 1] for row in t for i in range(len(row) - 1)]):
        return 'YES'
    return 'NO'