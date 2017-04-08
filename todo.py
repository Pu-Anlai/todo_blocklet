import os
import re
import todo_ui

HOME = os.environ['HOME']
TODO_PATH = os.path.join(HOME, '.local/share/todo.txt')
TODO_TXT = os.path.join(TODO_PATH, 'todo.txt.tmp')
DONE_TXT = os.path.join(TODO_PATH, 'done.txt')


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


task_dict = create_task_dict(TODO_TXT)
temp_dict = todo_ui.gui_from_tasks(task_dict)
for k, v in task_dict.items():
    print(k)
    for t in v:
        print(t)
