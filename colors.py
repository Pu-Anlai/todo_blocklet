# support global color settings for all blocklets set in a bash script one
# level up from todo_blocklet

import imp
import os
WORKING_DIR = os.path.dirname(os.path.realpath(__file__))
UP_DIR = os.path.abspath(os.path.join(WORKING_DIR, '..'))
try:
    imp.load_source('colors', '{}/colors'.format(UP_DIR))
    from colors import *
except FileNotFoundError:
    color01 = "#a3be8c"
    color02 = "#ebcb8b"
    color03 = "#d08770"
    color04 = "#bf616a"
