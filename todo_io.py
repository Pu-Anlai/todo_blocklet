#!/usr/bin/python

import re
import colors
import todo_rw
import todo_ui

task_dict = todo_rw.task_dict

task_int = len(todo_rw.extract_bare_tasks(task_dict))
urgent_int = len(task_dict['A'])
block_out = '{0!s}<span font_size ="small"> (<span color="{1}">{2!s}</span>)</span>'\
            .format(task_int, colors.color04, urgent_int)

print(block_out)
