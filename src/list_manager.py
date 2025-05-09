from models import TodoItem

class TodoManager:
    def __init__(self):
        self.todos = []

    def add_todo(self, todo_text: str) -> None:
        if todo_text.strip():
            self.todos.append(TodoItem(text=todo_text))

    def remove_todo(self, index: int) -> None:
        if 0 < index < len(self.todos):
            self.todos.remove(index)

    def toggle_completion(self, index: int) -> None:
        if 0 < index < len(self.todos):
            self.todos[index].completed = not self.todos[index].completed

    def clear(self) -> None:
        self.todos.clear()

    def get_all(self) -> list:
        return self.todos

