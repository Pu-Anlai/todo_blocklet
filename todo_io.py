import colors
import todo_rw
import todo_ui
from todo_config import TAIL_SGL_STR, TAIL_PL_STR


def tail(length):
    if length == 1:
        return TAIL_SGL_STR
    else:
        return TAIL_PL_STR


task_dict = todo_rw.task_dict

task_int = len(todo_rw.extract_bare_tasks(task_dict))
urgent_int = len(task_dict['A'])
block_out = ('{0!s}'
             '<span font_size ="small">'
             ' (<span color="{1}">{2!s}</span>)'
             ' {3}</span>').format(task_int,
                                   colors.color04,
                                   urgent_int,
                                   tail(task_int))

print(block_out)
