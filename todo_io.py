import os
import colors
import todo_rw
import todo_ui
from todo_config import TAIL_SGL_STR, TAIL_PL_STR

task_dict = todo_rw.task_dict


def tail(length):
    """Depending on length, return singular or plural trailing word."""
    if length == 1:
        return TAIL_SGL_STR
    else:
        return TAIL_PL_STR


def print_blocklet(task_dict):
    '''Print the string that is shown as output in i3blocks.'''
    task_int = len(todo_rw.extract_bare_tasks(task_dict))
    urgent_int = len(task_dict['A'])
    block_out = ('{0!s}'
                 '<span font_size ="small"> '
                 '(<span color="{1}">{2!s}</span>) '
                 '{3}</span>').format(task_int,
                                      colors.color04,
                                      urgent_int,
                                      tail(task_int))

    print(block_out)


def run_gui(task_dict):
    return_dict = todo_ui.gui_from_tasks(task_dict)
    if return_dict['exit_state'] == 0:
        todo_rw.apply_gui_changes(return_dict['done_tasks'],
                                  return_dict['rm_tasks'],
                                  task_dict)

    print_blocklet(task_dict)


try:
    if os.environ['BLOCK_BUTTON'] == '1':
        run_gui(task_dict)
except KeyError:
    print_blocklet(task_dict)
