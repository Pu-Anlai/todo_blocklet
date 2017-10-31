# [Todo.txt](http://todotxt.org/) blocklet

Put all these files in a folder and point the i3blocks config to that folder. Example:

    [todo.txt]
    command=python ${HOME}/.config/i3blocks/blocklets/todo.txt
    label=
    interval=60
    markup=pango

And then it looks something like this:

![Main Window](/images/main_window.png)

![Blocklet](/images/blocklet.png)


You can set the colors for the different categories in todo_markup.css. There's also todo_config.py which contains some instructions for configuration.

Anyway, I made this mainly for myself to learn about GUI creation with GTK. So if you're stumbling across this repository and actually want to use this but need some more instructions, just open an issue and I will extend this Readme.
