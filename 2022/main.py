from os import path

from tasks import d1, d2, d3, d4, d5, d6, d7, d8, d9
from task import Task


task_list = [
    d1.task,
    d2.task,
    d3.task,
    d4.task,
    d5.task,
    d6.task,
    d7.task,
    d8.task,
    d9.task,
]


def PrintResult(task: Task, answer1, answer2):
    print(
        f"Day {task.day}: {task.name} | Answer one: {answer1} | Answer two: {answer2}"
    )


def main():
    for task in task_list:
        task_path = path.join("input", str(task.day))
        if not path.exists(task_path):
            continue
        input1: list[str]
        with open(task_path) as f:
            input1 = f.read().splitlines()
        if not path.exists(task_path + "-2"):
            a1, a2 = task.solve(input1)
            PrintResult(task, a1, a2)
        else:
            input2: list[str]
            with open(task_path + "-2") as f:
                input2 = f.read().splitlines()
            a1, a2 = task.solve(input1, input2)
            PrintResult(task, a1, a2)


if __name__ == "__main__":
    main()
