from task import Task
import string


def solve(input: str):
    sum1 = 0
    sum2 = 0
    for rucksack in input:
        rucksack = rucksack.rstrip()
        half = len(rucksack) // 2
        for c in rucksack[:half]:
            if c in rucksack[half:]:
                sum1 += string.ascii_letters.index(c) + 1
                break
    # PART 2
    groups = [[]]
    for rucksack in input:
        rucksack = rucksack.rstrip()
        if len(groups[-1]) < 3:
            groups[-1].append(rucksack)
        else:
            groups.append([rucksack])
    for group in groups:
        for i in range(len(group)):
            rucksack: str = group.pop(i)
            for othersack in group:
                matches = ""
                for c in rucksack:
                    if c in othersack:
                        matches += c
                rucksack = matches
            if len(rucksack) != 0:
                sum2 += string.ascii_letters.index(rucksack[0]) + 1
                break
    return sum1, sum2


task = Task(3, "Rucksack Reorganization", solve)
