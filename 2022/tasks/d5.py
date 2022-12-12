from task import Task
import copy

def move_9000(count, stack_from, stack_to, stack_list):
    for i in range(int(count)):
        stack_list[int(stack_to)-1].append(stack_list[int(stack_from)-1].pop())

def move_9001(count, stack_from, stack_to, stack_list):
    crates = list[str]()
    for i in range(int(count)):
        crates.append(stack_list[int(stack_from)-1].pop())
    stack_list[int(stack_to)-1].extend(crates[::-1])


def solve(input: list[str]):
    stacks = list[list[str]]()
    for i in range((len(input[0])//4)+1):
        stacks.append(list[str]())
    instruction_start = -1
    for idx, line in enumerate(input):
        if '[' not in line:
            instruction_start = idx+2
            break
        for cidx, c in enumerate(line):
            if c == '[':
                stack_id = (cidx)//4
                stacks[stack_id].insert(0, line[cidx+1])

    stacks2 = copy.deepcopy(stacks) #use deepcopy for nested lists

    for idx in range(instruction_start, len(input)):
        parameters = input[idx].split(" ")[1::2]
        move_9000(parameters[0], parameters[1], parameters[2], stacks) #part1
        move_9001(parameters[0], parameters[1], parameters[2], stacks2) #part2

    stacks_res = ""
    stacks2_res = ""
    for stack in stacks:
        stacks_res += stack[-1]
    for stack in stacks2:
        stacks2_res += stack[-1]

    return stacks_res, stacks2_res

task = Task(5, "Supply Stacks", solve)