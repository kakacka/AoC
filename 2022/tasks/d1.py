from task import Task


def solve(input: list[str]):
    inventories = [0]
    idx = 0
    for calories in input:
        if len(calories) == 0:
            inventories.append(0)
            idx += 1
        else:
            inventories[idx] = inventories[idx] + int(calories)
    inventories.sort(reverse=True)
    top = inventories[0]
    top3 = inventories[0] + inventories[1] + inventories[2]
    return str(top), str(top3)


task = Task(1, "Calorie Counting", solve)
