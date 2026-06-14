import argparse

from utils.storage import load_data, save_data
from models.user import User
from models.project import Project
from models.task import Task

USERS_FILE = "data/users.json"
PROJECTS_FILE = "data/projects.json"
TASKS_FILE = "data/tasks.json"

def add_user(args):
    users = load_data(USERS_FILE)
    user = User(
        args.name,
        args.email
    )
    users.append(user.to_dict())
   
    save_data(USERS_FILE, users)
    print(f"User '{args.name}' created successfully")

def list_users(args):
    users = load_data(USERS_FILE)
    if not users:
        print("No users found.")
        return
    print("\nUsers:")
    for user in users:
        print(f"- {user['name']} ({user['email']})")

def add_project(args):
    projects = load_data(PROJECTS_FILE)

    project = Project(
        args.title,
        args.description,
        args.due_date,
        args.user
    )
    projects.append(project.to_dict())

    save_data(PROJECTS_FILE, projects)
    print(f"Project '{args.title}' added for {args.user}.")

def list_projects(args):
    projects = load_data(PROJECTS_FILE)
    user_projects = [
        p for p in projects if p["user"] == args.user
    ]
    if not user_projects:
        print(f"No projects found for {args.user}.")
        return
    print(f"\nProjects for {args.user}:")
    for p in user_projects:
        print(f"- {p['title']} | Due: {p['due_date']}")
def add_task(args):
    tasks = load_data(TASKS_FILE)
    task = Task(
        args.title,
        args.assigned_to
    )
    task_data = task.to_dict()
    task_data["project"] = args.project
    tasks.append(task_data)

    save_data(TASKS_FILE, tasks)
    print(f"Task '{args.title}' added to project '{args.project}'.")

def list_tasks (args):
    tasks = load_data(TASKS_FILE)
    project_tasks = [
        t for t in tasks if t.get("project") == args.project
    ]
    if not project_tasks:
        print(f"No tasks found for project '{args.project}'.")
        return
    print(f"\nTasks for project '{args.project}':")
    for t in project_tasks:
        print(f"- {t['title']} | {t['assigned_to']} | {t['status']}")

def complete_tasks(args):
    tasks = load_data(TASKS_FILE)
    for task_data in tasks:
        if task_data.get("title") == args.title:
            task =Task(
                task_data["title"],
                task_data["assigned_to"]
            )
            task.complete()
            task_data["status"] = task.status
            
            save_data(TASKS_FILE, tasks)
            print(f"Task '{args.title}' marked as completed.")
            return
        
        
    print(f"Task '{args.title}' not found")

def search_project(args):
    projects = load_data(PROJECTS_FILE)
    results =[
        p for p in projects
        if args.keyword.lower() in p["title"].lower()

    ]
    if not results:
        print("No matching projects found.")
        return
    print("\nSearch results:")
    for p in results:
        print(f"- {p['title']} (Owner: {p['user']})")

def main():
    parser = argparse.ArgumentParser(
        description ="Project Tracker CLI- Managing users, projects, and tasks" 
    )
    subparsers = parser.add_subparsers(dest="command")

    add_user_parser = subparsers.add_parser(
        "add-user",
        help="Create a new user"
    )
    add_user_parser.add_argument("--name", required=True)
    add_user_parser.add_argument("--email", required=True)
    add_user_parser.set_defaults(func=add_user)

    list_users_parser = subparsers.add_parser(
        "list-users",
        help ="List all users"
    )
    list_users_parser.set_defaults(func=list_users)

    add_project_parser = subparsers.add_parser(
        "add-project",
        help="Add a project to a user"
    )
    add_project_parser.add_argument("--user", required=True)
    add_project_parser.add_argument("--title", required=True)
    add_project_parser.add_argument("--description", required=True)
    add_project_parser.add_argument("--due-date", required=True)
    add_project_parser.set_defaults(func=add_project)

    list_projects_parser = subparsers.add_parser(
        "list-projects", help ="List projects for a user"
    )
    list_projects_parser.add_argument("--user", required=True)
    list_projects_parser.set_defaults(func=list_projects)

    add_task_parser = subparsers.add_parser(
        "add-task", help="Add a task to a project"
    )
    add_task_parser.add_argument("--project", required=True)
    add_task_parser.add_argument("--title", required=True)
    add_task_parser.add_argument("--assigned-to", required=True)
    add_task_parser.set_defaults(func=add_task)

    list_tasks_parser = subparsers.add_parser(
        "list-tasks",
        help="List tasks in a project"
    )
    list_tasks_parser.add_argument("--project", required=True)
    list_tasks_parser.set_defaults(func=list_tasks)
    complete_task_parser = subparsers.add_parser(
        "complete-task",
        help="Mark a task as completed"
    )
    complete_task_parser.add_argument("--title", required=True)
    complete_task_parser.set_defaults(func=complete_tasks)


    search_parser = subparsers.add_parser(
        "search-project", help="Search project by keyword"
    )
    search_parser.add_argument("--keyword", required=True)
    search_parser.set_defaults(func=search_project)

    args = parser.parse_args()
    
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__=="__main__":
    main()





