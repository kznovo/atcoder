N = int(input())
grid = [list(input()) for _ in range(N)]

for i in range(N - 2, -1, -1):
    for j in range(1, 2*N - 2):
        if all([
            grid[i][j] == "#",
            any([
                grid[i + 1][j - 1] == "X",
                grid[i + 1][j]     == "X",
                grid[i + 1][j + 1] == "X",
            ])
        ]):
            grid[i][j] = "X"

for row in grid:
    print("".join(row))
