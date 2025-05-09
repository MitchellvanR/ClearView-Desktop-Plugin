from dataclasses import dataclass

@dataclass
class TodoItem:
    text: str
    completed: bool = False

