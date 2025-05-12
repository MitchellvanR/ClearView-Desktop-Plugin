from dataclasses import dataclass

@dataclass
class ListItem:
    text: str
    completed: bool = False

