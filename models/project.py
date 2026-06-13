class Project:
    id_counter = 1

    def __init__(self, title, description, due_date, user):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.user = user
        
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append(task)
    
    def __repr__(self):
        return f"Project(id={self.id}, title='{self.title}')"