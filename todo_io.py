#!/usr/bin/python

import colors
import todo_rw
import todo_ui


# you can change these two to fit your own language (hopefully your language
# doesn't have dual marking on nouns)
tail_sgl_str = 'Task'
tail_pl_str = 'Tasks'


def tail(length):
    if length == 1:
        return tail_sgl_str
    else:
        return tail_pl_str


task_dict = todo_rw.task_dict

task_int = len(todo_rw.extract_bare_tasks(task_dict))
urgent_int = len(task_dict['A'])
block_out = ( '{0!s}'
              '<span font_size ="small">'
              ' (<span color="{1}">{2!s}</span>)'
              ' {3}</span>' ).format(task_int,
                                     colors.color04,
                                     urgent_int,
                                     tail(task_int))

print(block_out)
