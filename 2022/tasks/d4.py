from task import Task


def get_elf_assignments(elf: str) -> range:
    min, max = elf.split("-")
    return range(int(min), int(max) + 1)

def range_in_range(range1, range2):
    return range1.start >= range2.start and range1.stop <= range2.stop

def range_overlap(range1, range2):
    return range1[0] in range2 or range1[-1] in range2


def solve(input: str):
    sum = 0
    sum2 = 0
    for pair in input:
        elf1, elf2 = pair.split(",")
        ass1 = get_elf_assignments(elf1)
        ass2 = get_elf_assignments(elf2)
        if range_in_range(ass1, ass2) or range_in_range(ass2, ass1):
            sum += 1
        if range_overlap(ass1, ass2) or range_overlap(ass2, ass1):
            sum2 += 1

    return sum, sum2


task = Task(4, "Camp Cleanup", solve)
