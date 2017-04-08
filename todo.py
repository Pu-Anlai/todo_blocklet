import os
import re
from time import strftime
import todo_ui

HOME = os.environ['HOME']
TODO_PATH = os.path.join(HOME, '.local/share/todo.txt')
TODO_TXT = os.path.join(TODO_PATH, 'todo.txt.tmp')
DONE_TXT = os.path.join(TODO_PATH, 'done.txt.tmp')


def extract_cats(task_list):
    """Returns a set of all categories in TODO_TXT."""
    cats = re.findall(r'^\((\w)+\)', task_list, flags=re.MULTILINE)
    return sorted(set(cats))


def extract_cat_tasks(task_list, cat):
    """Return a list with all tasks of category $cat."""
    re_pattern = re.compile(r'^\({}\)\s+(.+)'.format(cat), flags=re.MULTILINE)
    ex_tasks = re.findall(re_pattern, task_list)
    ex_tasks.sort()
    return sorted(set(ex_tasks))


def extract_no_cat_tasks(task_list):
    """Return a list of all tasks with no assigned category."""
    ex_tasks = re.findall(r'^(?!\(\w\))(.+)', task_list, flags=re.MULTILINE)
    ex_tasks.sort()
    return sorted(set(ex_tasks))


def extract_bare_tasks(task_dict):
    """Extract a list of tasks without categories from task_dict."""
    bare_list = []
    for task_list in task_dict.values():
        for task in task_list:
            bare_list.append(task)

    return bare_list


def create_task_dict(in_file):
    """Parse in file and return a dictionary with categories as keys and a list
    of all tasks under the category as values."""
    with open(in_file, 'r') as todo_file:
        task_list = todo_file.read()
        task_dict = {}
        for cat in extract_cats(task_list):
            task_dict[cat] = extract_cat_tasks(task_list, cat)
            task_dict['none'] = extract_no_cat_tasks(task_list)

    return task_dict


def remove_tasks(remove_dict, task_dict):
    """Remove tasks from remove_dict in task_dict."""
    for cat, task_list in remove_dict.items():
        for task in task_list:
            task_dict[cat].remove(task)


def create_todo_items(task_dict):
    """Create a list of strings that can be written to todo.txt."""
    line_list = []
    for cat, task_list in task_dict.items():
        for task in task_list:
            line_list.append('({}) {}\n'.format(cat, task))

    return line_list


def create_done_items(done_dict):
    date = strftime('%Y-%m-%d')
    line_list = []
    for task in extract_bare_tasks(done_dict):
        line_list.append('x {} {}\n'.format(date, task))

    return line_list


def update_todo_file(in_file, task_dict):
    with open(in_file, 'w') as todo_file:
        for line in create_todo_items(task_dict):
            todo_file.write(line)


def update_done_file(in_file, done_list):
    with open(in_file, 'a') as done_file:
        for line in create_done_items(done_list):
            done_file.write(line)


task_dict = create_task_dict(TODO_TXT)
done_dict, rm_dict = todo_ui.gui_from_tasks(task_dict)
remove_tasks(done_dict, task_dict)
remove_tasks(rm_dict, task_dict)
update_todo_file(TODO_TXT, task_dict)
update_done_file(DONE_TXT, done_dict)
