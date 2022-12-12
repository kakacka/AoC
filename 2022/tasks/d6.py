from task import Task


class SimpleBuffer:  # circular buffer?
    buffer: str
    max_len: int

    def __init__(self, max_len: int):
        self.max_len = max_len
        self.buffer = ""

    def append(self, text: str):
        self.buffer += text
        while len(self.buffer) > self.max_len:
            self.buffer = self.buffer[1:]


def full_unique_buffer(buf: SimpleBuffer):
    return len(set(buf.buffer)) == buf.max_len


def solve(input: list[str]):
    res1 = 0
    res2 = 0
    buf1 = SimpleBuffer(4)
    buf2 = SimpleBuffer(14)

    for idx, c in enumerate(input[0]): #part1
        buf1.append(c)
        if full_unique_buffer(buf1):
            res1 = idx + 1
            break
    for idx, c in enumerate(input[0]): #part2
        buf2.append(c)
        if full_unique_buffer(buf2):
            res2 = idx + 1
            break

    return res1, res2


task = Task(6, "Tuning Trouble", solve)
