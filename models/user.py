from .person import Person

class User(Person):

    id_counter = 1
    def __init__(self, name, email):
        super().__init__(name)

        self.id = User.id_counter
        User.id_counter += 1

        self.email = email
        self.projects = []

    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError("Invalid email")
        self._email = value

    def add_project(self, project):
        self.projects.append(project)

    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}')"
 
