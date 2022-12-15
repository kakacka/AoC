from task import Task


def move_head(direction, head):
    if direction == "L":
        head[0] -= 1
    elif direction == "R":
        head[0] += 1
    elif direction == "U":
        head[1] += 1
    else:
        head[1] -= 1


def move_tail(tail, head):
    if abs(tail[0] - head[0]) <= 1 and abs(tail[1] - head[1]) <= 1:
        return False
    if tail[1] != head[1]:
        if tail[1] > head[1]:
            tail[1] -= 1
        else:
            tail[1] += 1
    if tail[0] != head[0]:
        if tail[0] > head[0]:
            tail[0] -= 1
        else:
            tail[0] += 1
    # assert abs(tail[0] - head[0]) <= 1 and abs(tail[1] - head[1]) <= 1, print(head, tail)
    return True


def solve(input: list[str]):
    visited_pos = {(0, 0)}
    head = [0, 0]
    tail = [0, 0]
    for row in input:
        direction = row[0]
        steps = int(row[2:])
        for _ in range(steps):
            move_head(direction, head)
            move_tail(tail, head)
            visited_pos.add((tail[0], tail[1]))

    visited_pos2 = {(0, 0)}
    rope = [[0, 0] for _ in range(10)]
    for row in input:
        direction = row[0]
        steps = int(row[2:])
        for _ in range(steps):
            move_head(direction, rope[0])
            cur_head = rope[0]
            for idx in range(1, len(rope)):
                if not move_tail(rope[idx], cur_head):
                    break
                cur_head = rope[idx]
            visited_pos2.add((rope[-1][0], rope[-1][1]))
    return len(visited_pos), len(visited_pos2)


task = Task(9, "Rope Bridge", solve)
