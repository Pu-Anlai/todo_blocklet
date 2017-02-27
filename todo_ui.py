import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk


class TodoWindow(Gtk.Window):

    def __init__(self, task_dict):
        Gtk.Window.__init__(self, title='Todo.txt')
        self.set_border_width(10)
        self.set_type_hint(Gdk.WindowTypeHint.DIALOG)
        self.vbox = Gtk.VBox(spacing=5)
        self.add(self.vbox)
        self.grid = Gtk.Grid(column_spacing=5, row_spacing=4)
        self.vbox.pack_start(self.grid, True, True, 0)

        screen = self.get_screen()
        css_provider = Gtk.CssProvider()
        css_provider.load_from_path('todo_markup.css')
        Gtk.StyleContext.\
            add_provider_for_screen(screen,
                                    css_provider,
                                    Gtk.STYLE_PROVIDER_PRIORITY_USER)

        self.populate_listbox(task_dict)

        separator = Gtk.Separator()
        self.vbox.pack_start(separator, True, True, 0)

        button_box = Gtk.ButtonBox(layout_style=Gtk.ButtonBoxStyle.SPREAD, spacing=2)
        self.vbox.pack_start(button_box, True, True, 0)

        ok_button = Gtk.Button.new_from_stock(Gtk.STOCK_OK)
        cancel_button = Gtk.Button.new_from_stock(Gtk.STOCK_CANCEL)
        button_box.add(cancel_button)
        button_box.add(ok_button)

        self.connect('delete-event', Gtk.main_quit)
        ok_button.connect('clicked', self.clicked_ok)
        cancel_button.connect('clicked', Gtk.main_quit)

    def populate_listbox(self, task_dict):
        categories = list(task_dict)
        categories.sort()
        pos = 0
        for cat in categories:
            self.populate_category(task_dict[cat], cat, pos)
            pos += len(task_dict[cat])

    def populate_category(self, task_list, category, pos):
        for index, task in enumerate(task_list):
            row = index + pos

            # the label that indicates if the task is marked as done or removed
            state_label = Gtk.Label(label='•', width_chars=2)
            self.grid.attach(state_label, 0, row, 1, 1)

            label = self.create_list_entry(task, category)
            label.default_category = category
            label.state = 'default'
            self.grid.attach_next_to(label, state_label,
                                     Gtk.PositionType.RIGHT,
                                     1, 1)

            done_button = Gtk.Button.new_from_icon_name('emblem-ok-symbolic',
                                                        Gtk.IconSize.BUTTON)
            done_button.pressed = False
            done_button.connect('clicked', self.clicked_done, row)

            rm_button = Gtk.Button.new_from_icon_name('edit-delete-symbolic',
                                                      Gtk.IconSize.BUTTON)
            rm_button.pressed = False
            rm_button.connect('clicked', self.clicked_rm, row)

            self.grid.attach_next_to(done_button, label,
                                     Gtk.PositionType.RIGHT,
                                     1, 1)
            self.grid.attach_next_to(rm_button, done_button,
                                     Gtk.PositionType.RIGHT,
                                     1, 1)

    def create_list_entry(self, task, css_class):
        label = Gtk.Label(task)
        label.get_style_context().add_class(css_class)
        label.set_alignment(0, .5)
        return label

    def clicked_done(self, button, row):
        label = self.get_label_in_grid(row)
        if not label.state == 'done':
            self.mark_task_done(row)
        else:
            self.mark_task_default(row)

    def clicked_rm(self, button, row):
        label = self.get_label_in_grid(row)
        if not label.state == 'removed':
            self.mark_task_removed(row)
        else:
            self.mark_task_default(row)

    def clicked_ok(self, button):
        Gtk.main_quit()

    def remove_css_classes(self, widget):
        context = widget.get_style_context()
        classes = context.list_classes()
        for css_class in classes:
            context.remove_class(css_class)

    def mark_task_done(self, row):
        label = self.get_label_in_grid(row)
        self.remove_css_classes(label)
        label.get_style_context().add_class('done')
        label.state = 'done'

        state_label = self.get_state_label_in_grid(row)
        state_label.set_label('✓')

    def mark_task_removed(self, row):
        label = self.get_label_in_grid(row)
        self.remove_css_classes(label)
        label.get_style_context().add_class('removed')
        label.state = 'removed'

        state_label = self.get_state_label_in_grid(row)
        state_label.set_label('✗')

    def mark_task_default(self, row):
        label = self.get_label_in_grid(row)
        self.remove_css_classes(label)
        category = label.default_category
        label.get_style_context().add_class(category)
        label.state = 'default'

        state_label = self.get_state_label_in_grid(row)
        state_label.set_label('•')

    def get_state_label_in_grid(self, row):
        state_label = self.grid.get_child_at(0, row)
        return state_label

    def get_label_in_grid(self, row):
        label = self.grid.get_child_at(1, row)
        return label

    def get_done_button_in_grid(self, row):
        done_button = self.grid.get_child_at(2, row)
        return done_button

    def get_rm_button_in_grid(self, row):
        rm_button = self.grid.get_child_at(3, row)
        return rm_button


def gui_from_tasks(task_dict):
    win = TodoWindow(task_dict)
    win.connect('delete-event', Gtk.main_quit)
    win.show_all()
    Gtk.main()
