from models.task import Task

def test_complete_task():
    task = Task(
        "Build CLI",
        "Alex"
    )
    task.complete()
    assert task.status == "Completed"
    