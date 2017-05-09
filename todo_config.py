import os

HOME = os.environ['HOME']

# Provide a path to the folder that contains your todo.txt and done.txt files
# here. The path is relative to your home directory. If that's not where you
# keep these files, just replace the entire line with an absolute path, like
# this:
# TODO_PATH = '/opt/user/something/todo.txt'
TODO_PATH = os.path.join(HOME, '.local/share/todo.txt')

# Here you can change the word appearing after the number of tasks in the
# blocklet output. There's two to differentiate between singular and plural
# (hopefully your language doesn't have dual marking on nouns).
TAIL_SGL_STR = 'Task'
TAIL_PL_STR = 'Tasks'
