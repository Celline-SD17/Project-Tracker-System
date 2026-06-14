# Project Tracker System
## Overview
- Project Tracker System is a Python Command-Line Interface (CLI) application that allows administrators to manage users, projects and tasks.
- It showcases python models such as one-to-many and many-to-many relationships, File I/O Models, Object Oriented Programming, and PyPi and Pip.
- The application supports:
    * Creating and listing users
    * Creating projects and assigning them to users
    * Creating tasks and assigning them to projects
    * Marking tasks as completed
    * Searching for projects
    * Persisting data using JSON files
    * Managing dependencies with pipenv and requirements.txt
    * Testing functionality using pytest

## Features
### User Management
- This facilitates:
    * Adding new users
    * Viewing all users
### Project Management
- This entails:
    * Creating projects
    * Assigning projects to users
    * Viewing projects by user
    * Searching projects by keyword
### Task Management
- This facilitates:
    * Adding tasks to projects
    * Assigning tasks to users
    * Marking tasks as completed
    * Viewing tasks for a project
### Data Persistence
- Data is stored locally using JSON files:
    * data/users.json
    * data/projects.json
    * data/tasks.json 
## Technologies used
- Python 3
- argparse
- json
- pytest
- Pipenv

## Installation
- Clone my github repository - ([[https://github.com/Celline-SD17/Project-Tracker-System]])
### Install dependencies
- Using requirements.txt:
    * In the terminal, enter command: pip install -r requirements.txt
- Or using Pipenv: 
    * pipenv install
## Project Structure

```
Project-Tracker-System/
│
├── main.py
├── Pipfile
├── Pipfile.lock
├── requirements.txt
│
├── data/
│   ├── users.json
│   ├── projects.json
│   └── tasks.json
│
├── models/
│   ├── __init__.py
│   ├── person.py
│   ├── user.py
│   ├── project.py
│   └── task.py
│
├── utils/
│   ├── __init__.py
│   └── storage.py
│
└── tests/
    ├── test_user.py
    ├── test_project.py
    └── test_task.py
```

## CLI Usage commands:

1. Add a User:
    * python3 main.py add-user --name "Alex" --email "alex@email.com"
2. List Users
    * python3 main.py list-users
3. Add a project
    * python3 main.py add-project --user "Alex" --title "CLI Tool" --description "School project" --due-date "2026-12-01"
4. List Projects
    * python3 main.py list-projects --user "Alex"
5. Add a Task
    * python3 main.py add-task --project "CLI Tool" --title "Implement add-task" --assigned-to "Alex"
6. View Tasks
    * python3 main.py list-tasks --project "CLI Tool"
7. Complete a Task
    * python3 main.py complete-task --title "Implement add-task"
8. Search for a Project
    * python3 main.py search-project --keyword "CLI"
9. View Available Commands
    * python3 main.py -h
## Running Tests
- You can run all tests together using:
    * pytest
- You can run each test file a a time using
    * pytest test/test_file.py eg pytest tests/test_user.py
## Author
- This project was developed as part of a Python learning project demonstrating Object Oriented Programming(OOP), inheritance and encapsulation, File Persitence with json, CLI using argparse, Unit Testing with Pytest, and Version control using Git and GitHub.
## License
- The project is mainly for educational purposes but can be used by firms for task management. 











