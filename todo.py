import os, re
import todo_ui

HOME = os.environ['HOME']
TODO_PATH = os.path.join(HOME, '.local/share/todo.txt')
TODO_TXT = os.path.join(TODO_PATH, 'todo.txt')
DONE_TXT = os.path.join(TODO_PATH, 'done.txt')


def extract_cats(task_list):
    """Returns a set of all categories in TODO_TXT."""
    cats = re.findall(r'^\(([^\)])+\)', task_list, flags=re.MULTILINE)
    return set(cats)


def extract_cat_tasks(task_list, cat):
    """Return a list with all tasks of category $cat."""
    re_pattern = re.compile(r'^\({}\)\s+(.+)'.format(cat), flags=re.MULTILINE)
    ex_tasks = re.findall(re_pattern, task_list)
    return ex_tasks


def extract_no_cat_tasks(task_list):
    """Return a list of all tasks with no assigned category."""
    ex_tasks = re.findall(r'^[^\(].+', task_list, flags=re.MULTILINE)
    return ex_tasks


def create_task_dict(in_file):
    """Parse in file and return a dictionary with categories as keys and a list
    of all tasks under the category as values."""
    with open(in_file, 'r') as todo_file:
        task_list = todo_file.read()
        task_dict = {}
        for cat in extract_cats(task_list):
            task_dict[cat] = extract_cat_tasks(task_list, cat)
    return task_dict


task_dict = create_task_dict(TODO_TXT)
todo_ui.gui_from_tasks(task_dict)
# for k, v in task_dict.items():
#     print(k)
#     print(v)


#     a_tasks = extract_cat_tasks(tasks, 'A')
#     b_tasks = extract_cat_tasks(tasks, 'B')
#     c_tasks = extract_cat_tasks(tasks, 'C')
#     no_tasks = extract_no_cat_tasks(tasks)
