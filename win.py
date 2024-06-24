"""Window."""
import tkinter
import tkinter.ttk
import sys


user_type = 'A'


def _(args):
    """_.

    :param args:
    """
    return args


class Application(tkinter.ttk.Frame):
    """Application."""

    def __init__(self, master=None):
        """__init__.

        :param master:
        """
        super().__init__(master)
        self.create_widgets()
        self.pack(expand=True, fill="both", padx=4, pady=4)
        self.master.title("TaskTracker")

    def on_conf_employees(self, evt):
        """on_conf_employees.

        :param evt:
        """
        self.canvas_employees.itemconfig(self.canvas_frame_employees, width=evt.width)

    def on_frame_conf_employees(self, evt):
        """on_frame_conf_employees.

        :param evt:
        """
        self.canvas_employees.configure(scrollregion=self.canvas_employees.bbox("all"))

    def on_conf_task(self, evt):
        """on_conf_task.

        :param evt:
        """
        self.canvas_task.itemconfig(self.canvas_frame_task, width=evt.width)

    def on_frame_conf_task(self, evt):
        """on_frame_conf_task.

        :param evt:
        """
        self.canvas_task.configure(scrollregion=self.canvas_task.bbox("all"))

    def on_conf_my_task(self, evt):
        """on_conf_my_task.

        :param evt:
        """
        self.canvas_my_task.itemconfig(self.canvas_frame_my_task, width=evt.width)

    def on_frame_conf_my_task(self, evt):
        """on_frame_conf_my_task.

        :param evt:
        """
        self.canvas_my_task.configure(scrollregion=self.canvas_my_task.bbox("all"))

    def on_conf_add_employees(self, evt):
        """on_conf_add_employees.

        :param evt:
        """
        self.canvas_add_employees.itemconfig(self.canvas_frame_add_employees, width=evt.width)

    def on_frame_conf_add_employees(self, evt):
        """on_frame_conf_add_employees.

        :param evt:
        """
        self.canvas_add_employees.configure(scrollregion=self.canvas_add_employees.bbox("all"))

    def on_conf_add_task(self, evt):
        """on_conf_add_task.

        :param evt:
        """
        self.canvas_add_task.itemconfig(self.canvas_frame_add_task, width=evt.width)

    def on_frame_conf_add_task(self, evt):
        """on_frame_conf_add_task.

        :param evt:
        """
        self.canvas_add_task.configure(scrollregion=self.canvas_add_task.bbox("all"))

    def create_widgets(self):
        """create_widgets."""
        ''' Notebook frame '''
        ntb = tkinter.ttk.Notebook(self)
        ntb.pack(fill="both", padx=4, pady=4, expand=True)
        ''' end '''

        ''' window on Notebook '''
        self.frame_employees = tkinter.ttk.Frame(ntb)
        self.frame_task = tkinter.ttk.Frame(ntb)
        self.frame_my_task = tkinter.ttk.Frame(ntb)
        ''' end '''

        ''' add '''
        ntb.add(self.frame_employees, text=_("Employees"), padding=4)
        ntb.add(self.frame_task, text=_("Task"), padding=4)
        ntb.add(self.frame_my_task, text=_("My Task"), padding=4)
        ''' end '''

        ''' scrollbar on self.employees '''
        self.canvas_employees = tkinter.Canvas(self.frame_employees)
        self.canvas_employees.pack(side='left', fill='both', expand=True)

        self.frame_employees_dop = tkinter.ttk.Frame(self.canvas_employees)

        self.canvas_frame_employees = self.canvas_employees.create_window((0, 0), \
                window=self.frame_employees_dop, anchor=tkinter.NW)

        self.scrollbar_employees = tkinter.ttk.Scrollbar(self.frame_employees, orient='vertical', \
                command=self.canvas_employees.yview)
        self.scrollbar_employees.pack(side='right', fill='y')

        self.canvas_employees.config(yscrollcommand=self.scrollbar_employees.set)

        self.frame_employees_dop.bind('<Configure>', self.on_frame_conf_employees)
        self.canvas_employees.bind('<Configure>', self.on_conf_employees)
        ''' end '''

        ''' scrollbar on self.frame_task '''
        self.canvas_task = tkinter.Canvas(self.frame_task)
        self.canvas_task.pack(side='left', fill='both', expand=True)

        self.frame_task_dop = tkinter.ttk.Frame(self.canvas_task)

        self.canvas_frame_task = self.canvas_task.create_window((0, 0), \
                window=self.frame_task_dop, anchor=tkinter.NW)

        self.scrollbar_task = tkinter.ttk.Scrollbar(self.frame_task, orient='vertical', \
                command=self.canvas_task.yview)
        self.scrollbar_task.pack(side='right', fill='y')

        self.canvas_task.config(yscrollcommand=self.scrollbar_task.set)

        self.frame_task_dop.bind('<Configure>', self.on_frame_conf_task)
        self.canvas_task.bind('<Configure>', self.on_conf_task)
        ''' end '''

        ''' scrollbar on self.frame_my_task '''
        self.canvas_my_task = tkinter.Canvas(self.frame_my_task)
        self.canvas_my_task.pack(side='left', fill='both', expand=True)

        self.frame_my_task_dop = tkinter.ttk.Frame(self.canvas_my_task)

        self.canvas_frame_my_task = self.canvas_my_task.create_window((0, 0), \
                window=self.frame_my_task_dop, anchor=tkinter.NW)

        self.scrollbar_my_task = tkinter.ttk.Scrollbar(self.frame_my_task, orient='vertical', \
                command=self.canvas_my_task.yview)
        self.scrollbar_my_task.pack(side='right', fill='y')

        self.canvas_my_task.config(yscrollcommand=self.scrollbar_my_task.set)

        self.frame_my_task_dop.bind('<Configure>', self.on_frame_conf_my_task)
        self.canvas_my_task.bind('<Configure>', self.on_conf_my_task)
        ''' end '''

        ''' fill the window in the Notebook '''
        self.widgets_employees()
        self.widgets_task()
        self.widgets_my_task()
        ''' end '''

        ''' some window for admin '''
        if user_type == 'B':
            return

        self.frame_add_employees = tkinter.ttk.Frame(ntb)
        self.frame_add_task = tkinter.ttk.Frame(ntb)

        ntb.add(self.frame_add_employees, text=_("Add Employees"), padding=4)
        ntb.add(self.frame_add_task, text=_("Add Task"), padding=4)
        ''' end '''

        ''' scrollbar on self.add_employees '''
        self.canvas_add_employees = tkinter.Canvas(self.frame_add_employees)
        self.canvas_add_employees.pack(side='left', fill='both', expand=True)

        self.frame_add_employees_dop = tkinter.ttk.Frame(self.canvas_add_employees)

        self.canvas_frame_add_employees = self.canvas_add_employees.create_window((0, 0), \
                window=self.frame_add_employees_dop, anchor=tkinter.NW)

        self.scrollbar_add_employees = tkinter.ttk.Scrollbar(self.frame_add_employees, orient='vertical', \
                command=self.canvas_add_employees.yview)
        self.scrollbar_add_employees.pack(side='right', fill='y')

        self.canvas_add_employees.config(yscrollcommand=self.scrollbar_add_employees.set)

        self.frame_add_employees_dop.bind('<Configure>', self.on_frame_conf_add_employees)
        self.canvas_add_employees.bind('<Configure>', self.on_conf_add_employees)
        ''' end '''

        ''' scrollbar on self.frame_add_task '''
        self.canvas_add_task = tkinter.Canvas(self.frame_add_task)
        self.canvas_add_task.pack(side='left', fill='both', expand=True)

        self.frame_add_task_dop = tkinter.ttk.Frame(self.canvas_add_task)

        self.canvas_frame_add_task = self.canvas_add_task.create_window((0, 0), \
                window=self.frame_add_task_dop, anchor=tkinter.NW)

        self.scrollbar_add_task = tkinter.ttk.Scrollbar(self.frame_add_task, orient='vertical', \
                command=self.canvas_add_task.yview)
        self.scrollbar_add_task.pack(side='right', fill='y')

        self.canvas_add_task.config(yscrollcommand=self.scrollbar_add_task.set)

        self.frame_add_task_dop.bind('<Configure>', self.on_frame_conf_add_task)
        self.canvas_add_task.bind('<Configure>', self.on_conf_add_task)
        ''' end '''

        ''' fill the window in the Notebook '''
        self.widgets_add_employees()
        self.widgets_add_task()
        ''' end '''

    def widgets_employees(self):
        """widgets_employees."""
        employees_info = [['228', 'Андрей Бутылкин', 'A'], ['186', 'Вячеслав Крет', 'B']]
        ''' TODO: заполнить employees_info '''

        self.lbl_employees = [[tkinter.ttk.Label(self.frame_employees_dop, text=_('ID')), 
                               tkinter.ttk.Label(self.frame_employees_dop, text=_('Name')),
                               tkinter.ttk.Label(self.frame_employees_dop, text=_('Type'))]]

        for user in employees_info:
            self.lbl_employees.append([])

            for info in user:
                self.lbl_employees[-1].append(tkinter.ttk.Label(self.frame_employees_dop, text=info))

        for i in range(3):
            self.frame_employees_dop.grid_columnconfigure(i, weight=1)

        for i in range(len(self.lbl_employees)):
            self.frame_employees_dop.grid_rowconfigure(i, weight=1)

            for j in range(3):
                self.lbl_employees[i][j].grid(row=i, column=j, padx=4, pady=4)

    def widgets_task(self):
        """widgets_task."""
        pass

    def widgets_my_task(self):
        """widgets_my_task."""
        pass

    def widgets_add_employees(self):
        """widgets_employees."""
        pass

    def widgets_add_task(self):
        """widgets_task."""
        pass


""" TODO: авторизация, проверка user_name, user_password
и добавление в user_type его тип 'B' -- zavod, 'A' иначе """

root = tkinter.Tk()
root.geometry("1280x720")
app = Application(root)
root.mainloop()
