# get colors from environment variables or use fall-back defaults

import os
color01 = "#{}".format(os.getenv("BASE0B") or "a3be8c")
color02 = "#{}".format(os.getenv("BASE0A") or "ebcb8b")
color03 = "#{}".format(os.getenv("BASE0F") or "d08770")
color04 = "#{}".format(os.getenv("BASE08") or "bf616a")
