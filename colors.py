import imp
import os
WORKING_DIR = os.path.dirname(os.path.realpath(__file__))
UP_DIR = os.path.abspath(os.path.join(WORKING_DIR, '..'))
imp.load_source('colors', '{}/colors'.format(UP_DIR))
from colors import * # i think this is a case where it's okay to do this
