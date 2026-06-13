class Task:
    id_counter = 1

    def __init__(self, title, assigned_to):
        self.id = Task.id_counter
        Task.id_counter +=1
        self.title = title
        self.assigned_to = assigned_to
        self.status = "Pending"

    def complete(self):
        self.status = "Completed"
    
    def __repr__(self):
        return f"Task(id={self.id}, title='{self.title}', status='{self.status}')"