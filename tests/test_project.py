from models.project import Project
from models.task import Task

def test_add_task():

    project = Project( 
        "CLI Tool",
        "School project",
        "2026-12-01",
        "Alex"
    )

    task = Task(
        "Build CLI",
        "Alex"
    )
    project.add_task(task)

    assert len(project.tasks) == 1