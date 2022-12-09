from dataclasses import dataclass
from typing import Callable


@dataclass
class Task:
    day: int
    name: str
    solve: Callable
