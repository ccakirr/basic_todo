# Task Manager CLI

A simple **Command Line Interface (CLI) Task Manager** built with Python.  
This program allows you to create a list of daily tasks, mark them as completed, and automatically save your progress in a history file.

---

## Features

- Add tasks for the current day.
- Mark tasks as completed.
- Save completed tasks to a daily history file (`YYYY-MM-DD_dids.txt`).
- Display pending and completed tasks in real-time.

---

## How It Works

1. Run the program.
2. Enter the number of tasks you have for the day.
3. Add each task one by one.
4. Complete tasks by entering their number.
5. Once all tasks are completed, you can check the daily history file to review them.

---

## Example Usage

$ python main.py
Please enter the count of today's missions.
3
Please enter the 1. mission.
Workout
Please enter the 2. mission.
Study Python
Please enter the 3. mission.
Read a book

Missions left:
1. Workout
2. Study Python
3. Read a book

Please enter the completed mission's number:
1
Mission 1 completed!
You have 2 mission(s) left.

---

## Project Structre
.
├── main.py
├── README.md
└── YYYY-MM-DD_dids.txt   # Generated daily when tasks are completed

## Requirements
Python 3.8 or higher

## Run the Project
Clone the repository:
git clone https://github.com/your-username/task-manager-cli.git

Navigate to the project folder:
cd task-manager-cli

Run the script:
python main.py

## Future Improvements
Save tasks in a JSON file for persistence.

Add a "delete task" feature.

Implement colored terminal output using rich library.

