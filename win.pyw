import tkinter
import tkinter.ttk


def _(args):
    return args


class Application(tkinter.ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets()
        self.pack(expand=True,fill="both", padx=4, pady=4)
        self.master.title("TaskTracker") 

    def on_conf_employees(self, evt):
        self.canvas_employees.itemconfig(self.canvas_frame_employees, width=evt.width)

    def on_frame_conf_employees(self, evt):
        self.canvas_employees.configure(scrollregion=self.canvas_employees.bbox("all"))


    def on_conf_task(self, evt):
        self.canvas_task.itemconfig(self.canvas_frame_task, width=evt.width)

    def on_frame_conf_task(self, evt):
        self.canvas_task.configure(scrollregion=self.canvas_task.bbox("all"))


    def on_conf_my_task(self, evt):
        self.canvas_my_task.itemconfig(self.canvas_frame_my_task, width=evt.width)

    def on_frame_conf_my_task(self, evt):
        self.canvas_my_task.configure(scrollregion=self.canvas_my_task.bbox("all"))


    def create_widgets(self):
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
        self.scrollbar_employees.pack(side='right', fill = 'y')

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
        self.scrollbar_task.pack(side='right', fill = 'y')

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
        self.scrollbar_my_task.pack(side='right', fill = 'y')

        self.canvas_my_task.config(yscrollcommand=self.scrollbar_my_task.set)


        self.frame_my_task_dop.bind('<Configure>', self.on_frame_conf_my_task)
        self.canvas_my_task.bind('<Configure>', self.on_conf_my_task)
        ''' end '''


        ''' fill the window in the Notebook '''
        self.widgets_employees()
        self.widgets_task()
        self.widgets_my_task()
        ''' end '''

        
    def widgets_employees(self):
        pass

    def widgets_task(self):
        pass

    def widgets_my_task(self):
        pass


root = tkinter.Tk()
root.geometry("1280x720")
app = Application(root)
root.mainloop()
