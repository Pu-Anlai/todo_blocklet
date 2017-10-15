import os
import subprocess
import colors
import todo_rw
import todo_ui
from todo_config import TAIL_SGL_STR, TAIL_PL_STR, TXT_EDITOR

task_dict = todo_rw.task_dict


def tail(length):
    """Depending on length, return singular or plural trailing word."""
    if length == 1:
        return TAIL_SGL_STR
    else:
        return TAIL_PL_STR


def critical_str(urgent_int, color):
    '''Return a string for critical tasks only if there are any.'''
    if urgent_int > 0:
        return '(<span color="{0}">{1!s}</span>)'.format(color, urgent_int)
    else:
        return ''


def print_blocklet(task_dict):
    '''Print the string that is shown as output in i3blocks.'''
    try:
        task_int = len(todo_rw.extract_bare_tasks(task_dict))
    except KeyError:
        task_int = 0

    try:
        urgent_int = len(task_dict['A'])
    except KeyError:
        urgent_int = 0

    block_out = ('{0!s}'
                 '<span font_size ="small">'
                 ' {1} '
                 '{2}</span>').format(task_int,
                                      critical_str(urgent_int, colors.color04),
                                      tail(task_int))

    print(block_out)


def run_gui(task_dict):
    return_dict = todo_ui.gui_from_tasks(task_dict)
    if return_dict['exit_state'] == 0:
        todo_rw.apply_gui_changes(return_dict['done_tasks'],
                                  return_dict['rm_tasks'],
                                  task_dict)


def open_in_editor(txt_file):
    subprocess.run(TXT_EDITOR.format(txt_file), shell=True)
    # subprocess.run([TXT_EDITOR, txt_file])


if os.environ['BLOCK_BUTTON'] == '1':
    run_gui(task_dict)
elif os.environ['BLOCK_BUTTON'] == '2':
    open_in_editor(todo_rw.TODO_TXT)

print_blocklet(task_dict)
