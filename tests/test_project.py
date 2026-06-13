from models.project import Project

def test_create_project():
    project = Project( 
        "CLI Tool",
        "School project",
        "2026-12-01",
        "Alex"
    )
    assert project.title == "CLI Tool"