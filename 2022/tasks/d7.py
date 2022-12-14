from task import Task


def nested_get(dic, keys):
    for key in keys:
        dic = dic[key]
    return dic


def find_all_dir_max_size(dir: dict, max_size: int, size_list: list) -> int:
    size = 0
    for key, val in dir.items():
        if type(val) is dict:
            size += find_all_dir_max_size(val, max_size, size_list)
        else:
            size += val
    if size <= max_size:
        size_list.append(size)
    return size


def find_all_dir_min_size(dir: dict, min_size: int, size_list: list) -> int:
    size = 0
    for key, val in dir.items():
        if type(val) is dict:
            size += find_all_dir_min_size(val, min_size, size_list)
        else:
            size += val
    if size >= min_size:
        size_list.append(size)
    return size


def solve(input: list[str]):
    root = {}
    currentPath = []

    for line in input:
        sline = line.split(" ")
        if sline[0] == "$":
            if sline[1] == "cd":
                if sline[2] == "/":
                    currentPath = []
                elif sline[2] == "..":
                    currentPath.pop()
                else:
                    if nested_get(root, currentPath).get(sline[2]) is None:
                        nested_get(root, currentPath)[sline[2]] = {}
                    currentPath.append(sline[2])
            else:
                pass
        elif sline[0] == "dir":
            if nested_get(root, currentPath).get(sline[1]) is None:
                nested_get(root, currentPath)[sline[1]] = {}
        else:
            if nested_get(root, currentPath).get(sline[1]) is None:
                nested_get(root, currentPath)[sline[1]] = int(sline[0])

    size_list_max = list[int]()
    size_list_min = list[int]()
    totalsize = find_all_dir_max_size(root, 100000, size_list_max)
    find_all_dir_min_size(root, 30000000 - (70000000 - totalsize), size_list_min)
    return sum(size_list_max), min(size_list_min)


task = Task(7, "No Space Left On Device", solve)
