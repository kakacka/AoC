from task import Task


def scenic_score(tree, x, y, row, col):
    if x == 0 or x + 1 == len(row) or y == 0 or y + 1 == len(col):
        return 0
    left = 1
    right = 1
    up = 1
    down = 1
    for i in range(1, x + 1):  # left
        left = i
        if row[x - i] >= tree:
            break
    for i in range(1, len(row) - x):  # right
        right = i
        if row[x + i] >= tree:
            break
    for i in range(1, y + 1):  # up
        up = i
        if col[y - i] >= tree:
            break
    for i in range(1, len(col) - y):  # down
        down = i
        if col[y + i] >= tree:
            break
    return left * right * up * down


def solve(input: list[str]):
    visible_count = 0
    max_score = 0
    for y, row in enumerate(input):  # part1
        for x, tree in enumerate(row):
            if (
                x == 0
                or x + 1 == len(row)
                or y == 0
                or y + 1 == len(input)
                or all([t < tree for t in row[:x]])  # left
                or all([t < tree for t in row[x + 1 :]])  # right
                or all([t[x] < tree for t in input[:y]])  # up
                or all([t[x] < tree for t in input[y + 1 :]])  # down
            ):
                visible_count += 1

    for y, row in enumerate(input):  # part2
        for x, tree in enumerate(row):
            score = scenic_score(tree, x, y, row, [r[x] for r in input])
            if score > max_score:
                max_score = score
    return visible_count, max_score


task = Task(8, "Treetop Tree House", solve)
