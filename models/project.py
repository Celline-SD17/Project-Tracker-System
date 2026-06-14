class Project:
    id_counter = 1

    def __init__(self, title, description, due_date, user):
        self.id = Project.id_counter
        Project.id_counter += 1
        self.title = title
        self.description = description
        self.due_date = due_date
        self.user = user
        
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append(task)
    
    def task_count(self):
        return len(self.tasks)
    
    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "user": self.user,
        }

    def __repr__(self):
        return f"Project(id={self.id}, title='{self.title}')"