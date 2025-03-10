class Todo :
    def __init__(self, code_id: int, title: str, description: str):
        self.code_id: int = code_id
        self.title: str = title
        self.description: str = description
        self.completed: bool = False
        self.tags : list[str] = []

    def mark_completed(self):
        self.completed = True

    def add_tag(self, tag:str):
        tags = []
        if tag not in tags:
            self.tags.append(tag)

    def __str__(self)-> str:
        return f"{self.code_id} - {self.title}"

class TodoBook:
    def __init__(self ):
        self.todos: dict[int, Todo] = {}

    def add_todo(self, title:str , description:str)-> int:
        code_id = len(self.todos)+1


    def pending_todos(self):
        pass

    def completed_todos(self):
        pass

    def tags_todo_count(self):
        pass






