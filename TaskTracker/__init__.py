"""Window."""
import tkinter
import tkinter.ttk
from tkinter import messagebox as mb
import os
import gettext
import locale
from . import scripts
import psycopg2
import sys
from datetime import datetime

user_type = 'B'
worker_id = 0

_podir = os.path.join('/'.join(os.path.dirname(__file__).split('/')), "po")

TRANSLATIONS = {
    ("ru_RU", "UTF-8"): gettext.translation("msg", _podir, ["ru_RU.UTF-8"]),
    ("en_US", "UTF-8"): gettext.NullTranslations(),
}


def _(text):
    """_.

    :param text:
    """
    return TRANSLATIONS[locale.getlocale()].gettext(text)


class Application(tkinter.ttk.Frame):
    """Application."""

    def __init__(self, master=None):
        """__init__.

        :param master:
        """
        super().__init__(master)

        self.lng_set = tkinter.IntVar()
        self.lng_set.set(0)  # 0--English, 1--Russian

        self.create_widgets()
        self.pack(expand=True, fill="both", padx=4, pady=4)
        self.master.title("TaskTracker")

    def update_foo(self):
        """update_foo."""
        self.ntb.destroy()
        self.create_widgets()

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

    def on_conf_commit_progress(self, evt):
        """on_conf_commit_progress.

        :param evt:
        """
        self.canvas_commit_progress.itemconfig(self.canvas_frame_commit_progress, width=evt.width)

    def on_frame_conf_commit_progress(self, evt):
        """on_frame_conf_commit_progress.

        :param evt:
        """
        self.canvas_commit_progress.configure(scrollregion=self.canvas_commit_progress.bbox("all"))

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

    def on_conf_del_employees(self, evt):
        """on_conf_del_employees.

        :param evt:
        """
        self.canvas_del_employees.itemconfig(self.canvas_frame_del_employees, width=evt.width)

    def on_frame_conf_del_employees(self, evt):
        """on_frame_conf_del_employees.

        :param evt:
        """
        self.canvas_del_employees.configure(scrollregion=self.canvas_del_employees.bbox("all"))

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

    def on_conf_del_task(self, evt):
        """on_conf_del_task.

        :param evt:
        """
        self.canvas_del_task.itemconfig(self.canvas_frame_del_task, width=evt.width)

    def on_frame_conf_del_task(self, evt):
        """on_frame_conf_del_task.

        :param evt:
        """
        self.canvas_del_task.configure(scrollregion=self.canvas_del_task.bbox("all"))

    def create_widgets(self):
        """create_widgets."""
        if self.lng_set.get():
            locale.setlocale(locale.LC_ALL, ('ru_RU', 'UTF-8'))
        else:
            locale.setlocale(locale.LC_ALL, ('en_US', 'UTF-8'))

        main_menu = tkinter.Menu(self.master)
        self.master['menu'] = main_menu

        settings_menu = tkinter.Menu(main_menu, tearoff=False)
        settings_menu.add_command(label=_('Update Info'), command=self.update_foo)
        settings_menu.add_command(label=_('Quit'), command=self.master.destroy)

        main_menu.add_cascade(label=_('Settings'), menu=settings_menu)

        language_menu = tkinter.Menu(main_menu, tearoff=False)

        language_menu.add_radiobutton(label="English", variable=self.lng_set, value=0, command=self.update_foo)
        language_menu.add_radiobutton(label="Русский", variable=self.lng_set, value=1, command=self.update_foo)

        main_menu.add_cascade(label=_('Language'), menu=language_menu)

        ''' Notebook frame '''
        self.ntb = tkinter.ttk.Notebook(self)
        self.ntb.pack(fill="both", padx=4, pady=4, expand=True)
        ''' end '''

        ''' window on Notebook '''
        self.frame_employees = tkinter.ttk.Frame(self.ntb)
        self.frame_task = tkinter.ttk.Frame(self.ntb)
        self.frame_my_task = tkinter.ttk.Frame(self.ntb)
        self.frame_commit_progress = tkinter.ttk.Frame(self.ntb)
        ''' end '''

        ''' add '''
        self.ntb.add(self.frame_employees, text=_("Employees"), padding=4)
        self.ntb.add(self.frame_task, text=_("Tasks"), padding=4)
        self.ntb.add(self.frame_my_task, text=_("My Tasks"), padding=4)
        self.ntb.add(self.frame_commit_progress, text=_("Commit Progress"), padding=4)
        ''' end '''

        ''' scrollbar on self.employees '''
        self.canvas_employees = tkinter.Canvas(self.frame_employees)
        self.canvas_employees.pack(side='left', fill='both', expand=True)

        self.frame_employees_dop = tkinter.ttk.Frame(self.canvas_employees)

        self.canvas_frame_employees = self.canvas_employees.create_window((0, 0), \
                                                                          window=self.frame_employees_dop,
                                                                          anchor=tkinter.NW)

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

        ''' scrollbar on self.frame_commit_progress '''
        self.canvas_commit_progress = tkinter.Canvas(self.frame_commit_progress)
        self.canvas_commit_progress.pack(side='left', fill='both', expand=True)

        self.frame_commit_progress_dop = tkinter.ttk.Frame(self.canvas_commit_progress)

        self.canvas_frame_commit_progress = self.canvas_commit_progress.create_window((0, 0),
                                        window=self.frame_commit_progress_dop, anchor=tkinter.NW)

        self.scrollbar_commit_progress = tkinter.ttk.Scrollbar(self.frame_commit_progress, orient='vertical', \
                                                               command=self.canvas_commit_progress.yview)
        self.scrollbar_commit_progress.pack(side='right', fill='y')

        self.canvas_commit_progress.config(yscrollcommand=self.scrollbar_commit_progress.set)

        self.frame_commit_progress_dop.bind('<Configure>', self.on_frame_conf_commit_progress)
        self.canvas_commit_progress.bind('<Configure>', self.on_conf_commit_progress)
        ''' end '''

        ''' fill the window in the Notebook '''
        self.widgets_employees()
        self.widgets_task()
        self.widgets_my_task()
        self.widgets_commit_progress()
        ''' end '''

        ''' some window for admin '''
        if user_type == 'B':
            return

        self.frame_add_employees = tkinter.ttk.Frame(self.ntb)
        self.frame_add_task = tkinter.ttk.Frame(self.ntb)
        self.frame_del_employees = tkinter.ttk.Frame(self.ntb)
        self.frame_del_task = tkinter.ttk.Frame(self.ntb)

        self.ntb.add(self.frame_add_employees, text=_("Add Employee"), padding=4)
        self.ntb.add(self.frame_del_employees, text=_("Delete Employee"), padding=4)
        self.ntb.add(self.frame_add_task, text=_("Add Task"), padding=4)
        self.ntb.add(self.frame_del_task, text=_("Delete Task"), padding=4)
        ''' end '''

        ''' scrollbar on self.add_employees '''
        self.canvas_add_employees = tkinter.Canvas(self.frame_add_employees)
        self.canvas_add_employees.pack(side='left', fill='both', expand=True)

        self.frame_add_employees_dop = tkinter.ttk.Frame(self.canvas_add_employees)

        self.canvas_frame_add_employees = self.canvas_add_employees.create_window((0, 0), \
                                                                                  window=self.frame_add_employees_dop,
                                                                                  anchor=tkinter.NW)

        self.scrollbar_add_employees = tkinter.ttk.Scrollbar(self.frame_add_employees, orient='vertical', \
                                                             command=self.canvas_add_employees.yview)
        self.scrollbar_add_employees.pack(side='right', fill='y')

        self.canvas_add_employees.config(yscrollcommand=self.scrollbar_add_employees.set)

        self.frame_add_employees_dop.bind('<Configure>', self.on_frame_conf_add_employees)
        self.canvas_add_employees.bind('<Configure>', self.on_conf_add_employees)
        ''' end '''

        ''' scrollbar on self.del_employees '''
        self.canvas_del_employees = tkinter.Canvas(self.frame_del_employees)
        self.canvas_del_employees.pack(side='left', fill='both', expand=True)

        self.frame_del_employees_dop = tkinter.ttk.Frame(self.canvas_del_employees)

        self.canvas_frame_del_employees = self.canvas_del_employees.create_window((0, 0), \
                                                                                  window=self.frame_del_employees_dop,
                                                                                  anchor=tkinter.NW)

        self.scrollbar_del_employees = tkinter.ttk.Scrollbar(self.frame_del_employees, orient='vertical', \
                                                             command=self.canvas_del_employees.yview)
        self.scrollbar_del_employees.pack(side='right', fill='y')

        self.canvas_del_employees.config(yscrollcommand=self.scrollbar_del_employees.set)

        self.frame_del_employees_dop.bind('<Configure>', self.on_frame_conf_del_employees)
        self.canvas_del_employees.bind('<Configure>', self.on_conf_del_employees)
        ''' end '''

        ''' scrollbar on self.frame_add_task '''
        self.canvas_add_task = tkinter.Canvas(self.frame_add_task)
        self.canvas_add_task.pack(side='left', fill='both', expand=True)

        self.frame_add_task_dop = tkinter.ttk.Frame(self.canvas_add_task)

        self.canvas_frame_add_task = self.canvas_add_task.create_window((0, 0), \
                                                                        window=self.frame_add_task_dop,
                                                                        anchor=tkinter.NW)

        self.scrollbar_add_task = tkinter.ttk.Scrollbar(self.frame_add_task, orient='vertical', \
                                                        command=self.canvas_add_task.yview)
        self.scrollbar_add_task.pack(side='right', fill='y')

        self.canvas_add_task.config(yscrollcommand=self.scrollbar_add_task.set)

        self.frame_add_task_dop.bind('<Configure>', self.on_frame_conf_add_task)
        self.canvas_add_task.bind('<Configure>', self.on_conf_add_task)
        ''' end '''

        ''' scrollbar on self.frame_del_task '''
        self.canvas_del_task = tkinter.Canvas(self.frame_del_task)
        self.canvas_del_task.pack(side='left', fill='both', expand=True)

        self.frame_del_task_dop = tkinter.ttk.Frame(self.canvas_del_task)

        self.canvas_frame_del_task = self.canvas_del_task.create_window((0, 0), \
                                                                        window=self.frame_del_task_dop,
                                                                        anchor=tkinter.NW)

        self.scrollbar_del_task = tkinter.ttk.Scrollbar(self.frame_del_task, orient='vertical', \
                                                        command=self.canvas_del_task.yview)
        self.scrollbar_del_task.pack(side='right', fill='y')

        self.canvas_del_task.config(yscrollcommand=self.scrollbar_del_task.set)

        self.frame_del_task_dop.bind('<Configure>', self.on_frame_conf_del_task)
        self.canvas_del_task.bind('<Configure>', self.on_conf_del_task)
        ''' end '''

        ''' fill the window in the Notebook '''
        self.widgets_add_employees()
        self.widgets_del_employees()
        self.widgets_add_task()
        self.widgets_del_task()
        ''' end '''

    def widgets_employees(self):
        """widgets_employees."""
        employees_info = sorted(list(scripts.workers_and_types_script()), key=lambda x: x[0])
        # employees_info = [['228', 'Андрей Бутылкин', 'A'], ['186', 'Вячеслав Крет', 'B']]
        ''' TODO: заполнить employees_info '''

        self.lbl_employees = [[tkinter.ttk.Label(self.frame_employees_dop, text=_('ID'), font=('Arial', 16)),
                               tkinter.ttk.Label(self.frame_employees_dop, text=_('Name'), font=('Arial', 16)),
                               tkinter.ttk.Label(self.frame_employees_dop, text=_('Type'), font=('Arial', 16))]]

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
        task_info = sorted(list(map(lambda x: list(x), scripts.all_tasks_script())), key=lambda x: x[0])
        # task_info = [['001', 'TaskTracker', '228', ['186'], '20', '28.06.2024']]
        ''' TODO: заполнить task_info '''

        self.lbl_task = [[tkinter.ttk.Label(self.frame_task_dop, text=_('ID'), font=('Arial', 16)),
                          tkinter.ttk.Label(self.frame_task_dop, text=_('Task Name'), font=('Arial', 16)),
                          tkinter.ttk.Label(self.frame_task_dop, text=_('Supervisor'), font=('Arial', 16)),
                          tkinter.ttk.Label(self.frame_task_dop, text=_('Workers'), font=('Arial', 16)),
                          tkinter.ttk.Label(self.frame_task_dop, text=_('Completion Percentage'), font=('Arial', 16)),
                          tkinter.ttk.Label(self.frame_task_dop, text=_('Deadline'), font=('Arial', 16))]]

        for task in task_info:
            self.lbl_task.append([])

            for info in task:
                self.lbl_task[-1].append(tkinter.ttk.Label(self.frame_task_dop, text=info))

        for i in range(6):
            self.frame_task_dop.grid_columnconfigure(i, weight=1)

        for i in range(len(self.lbl_task)):
            self.frame_task_dop.grid_rowconfigure(i, weight=1)

            for j in range(6):
                self.lbl_task[i][j].grid(row=i, column=j, padx=4, pady=4)

    def widgets_my_task(self):
        """widgets_my_task."""
        # print(list(scripts.all_tasks_by_worker_id(worker_id)))
        my_task_info = []
        if user_type == 'A':
            my_task_info += list(scripts.all_tasks_by_supervisor(worker_id))
        my_task_info += list(scripts.all_tasks_by_worker_id(worker_id))
        # my_task_info = [['001', 'TaskTracker', '20', '28.06.2024', "Description: need to close the 3rd course", \
        #                 [['228', '10', 'labudabdab'], ['186', '20', 'a']]]]
        ''' TODO: заполнить my_task_info '''
        self.lbl_frame_my_task = []

        for task in sorted(my_task_info, key=lambda x: x[0]):
            style = tkinter.ttk.Style()
            style.configure('Custom.TLabelframe.Label', font=('Arial', 16))

            self.lbl_frame_my_task.append(tkinter.ttk.LabelFrame(self.frame_my_task_dop, text=_('task_id: {}, ' + \
                                                    'task_name: {}, completion_percentage: {}, deadline: {}').format(
                task[0], \
                task[1], task[2], task[3]), labelanchor='n', style="Custom.TLabelframe"))

            self.lbl_frame_my_task[-1].pack(expand=True, fill="both", padx=14, pady=14)

            for i in range(3):
                self.lbl_frame_my_task[-1].grid_columnconfigure(i, weight=1)

            lbl_my_task_description = tkinter.ttk.Label(self.lbl_frame_my_task[-1], text=task[4])
            lbl_my_task_description.grid(row=0, columnspan=3, padx=4, pady=4)

            lbl_my_task_i = [[tkinter.ttk.Label(self.lbl_frame_my_task[-1], text=_('ID'), font=('Arial', 16)),
                              tkinter.ttk.Label(self.lbl_frame_my_task[-1], text=_('Completion Percentage'),
                                                font=('Arial', 16)),
                              tkinter.ttk.Label(self.lbl_frame_my_task[-1], text=_('Description'), font=('Arial', 16))]]

            for entry in task[5]:
                lbl_my_task_i.append([])

                for info in entry:
                    lbl_my_task_i[-1].append(tkinter.ttk.Label(self.lbl_frame_my_task[-1], text=info))

            for i in range(len(lbl_my_task_i)):
                self.lbl_frame_my_task[-1].grid_rowconfigure(i + 1, weight=1)

                for j in range(3):
                    lbl_my_task_i[i][j].grid(row=i + 1, column=j, padx=4, pady=4)

    def widgets_commit_progress(self):
        """widgets_commit_progress."""

        def on_enter_press(event):
            """on_enter_press.

            :param event:
            """
            self.txt_description.insert(tkinter.END, '\n')
            self.txt_description.see(tkinter.END)

        lbl_task_id = tkinter.ttk.Label(self.frame_commit_progress_dop, text=_('Task ID'), font=('Arial', 16))
        lbl_percent = tkinter.ttk.Label(self.frame_commit_progress_dop, text=_('Completion Percentage'), \
                                        font=('Arial', 16))
        lbl_description = tkinter.ttk.Label(self.frame_commit_progress_dop, text=_('Description'), font=('Arial', 16))

        self.vr_task_id = tkinter.StringVar()
        self.vr_percent = tkinter.IntVar()
        self.vr_percent.set(0)

        lbl_task_id.pack(expand=True, fill="none", padx=10, pady=10)
        ntr_task_id = tkinter.ttk.Entry(self.frame_commit_progress_dop, textvariable=self.vr_task_id)
        ntr_task_id.pack(expand=True, fill="none", padx=10, pady=10)

        lbl_percent.pack(expand=True, fill="none", padx=10, pady=10)
        spn_percent = tkinter.Spinbox(self.frame_commit_progress_dop, textvariable=self.vr_percent, from_=0, \
                                      to=100, increment=1, exportselection=0)
        spn_percent.pack(expand=True, fill="none", padx=10, pady=10)

        lbl_description.pack(expand=True, fill="none", padx=10, pady=10)
        self.txt_description = tkinter.Text(self.frame_commit_progress_dop, wrap='word', height=10, width=40)
        self.txt_description.pack(expand=True, fill="both", padx=10, pady=10)
        self.txt_description.bind('<Return>', on_enter_press)

        btn_commit = tkinter.ttk.Button(self.frame_commit_progress_dop, text=_("Commit"), command=self.commit_db)
        btn_commit.pack(expand=True, fill="none", padx=10, pady=10)

    def commit_db(self):
        """commit_db."""
        """TODO: занести в базу данных всю информацию о новой записи, проверить корректность введенных данных"""
        # self.txt_description.get("1.0", tkinter.END)
        task_id = self.vr_task_id.get()
        percent = self.vr_percent.get()
        # print(self.txt_task_description.get('1.0'))
        descr = self.txt_description.get("1.0", tkinter.END)
        try:
            conn = psycopg2.connect("dbname = 'db_task' user = 'postgres' host='localhost' password='0852'")
        except Exception as e:
            print(f'Undefined error {e}')

        with conn.cursor() as curs:
            curs.execute("SELECT task_id FROM task_info")
            q = list(map(lambda x: x[0], curs.fetchall()))
            if int(task_id) not in q:
                mb.showerror("Error!", f"Task with ID {task_id} doesnt exist")
            elif not 0 <= percent <= 100:
                mb.showerror("Error!", "Percent is a number between 0 and 100")
            else:
                curs.execute("SELECT task_workers FROM task_info")
                q = list(map(lambda x: x[0], curs.fetchall()))
                if worker_id not in q:
                    mb.showerror("Error!", "You cant commit progress in this project")
                else:
                    curs.execute(f"""
                        UPDATE task_info
                        SET percent = {percent}
                        WHERE task_id = {task_id};
                        COMMIT
                        """)

                    curs.execute("SELECT entry_id FROM task_entry")
                    counter = 0
                    flag = True
                    for i in sorted(curs.fetchall()):
                        if i[0] != counter:
                            entry_id = counter
                            flag = False
                            break
                        counter += 1
                    if flag:
                        entry_id = counter

                    curs.execute(f"""
                        INSERT INTO task_entry (entry_id,task_id,workers_id,entry_description,percent,date) VALUES
                            ({entry_id},{task_id},{worker_id},'{descr}',{percent},'{datetime.now()}');
                        COMMIT
                        """)

                    # после этого выполняется следующий блок код

                    self.update_foo()

    def widgets_add_employees(self):
        """widgets_employees."""
        lbl_user_name = tkinter.ttk.Label(self.frame_add_employees_dop, text=_('Name'), font=('Arial', 16))
        lbl_user_password = tkinter.ttk.Label(self.frame_add_employees_dop, text=_('Password'), font=('Arial', 16))
        lbl_user_type = tkinter.ttk.Label(self.frame_add_employees_dop, text=_('Type'), font=('Arial', 16))

        self.vr_user_name = tkinter.StringVar()
        self.vr_user_password = tkinter.StringVar()

        lbl_user_name.pack(expand=True, fill="none", padx=10, pady=10)
        ntr_user_name = tkinter.ttk.Entry(self.frame_add_employees_dop, textvariable=self.vr_user_name)
        ntr_user_name.pack(expand=True, fill="none", padx=10, pady=10)

        lbl_user_password.pack(expand=True, fill="none", padx=10, pady=10)
        ntr_user_password = tkinter.ttk.Entry(self.frame_add_employees_dop, textvariable=self.vr_user_password)
        ntr_user_password.pack(expand=True, fill="none", padx=10, pady=10)

        lbl_user_type.pack(expand=True, fill="none", padx=10, pady=10)
        self.lst_user_type = tkinter.Listbox(self.frame_add_employees_dop, width=3, height=2, exportselection=0, \
                                             activestyle='dotbox')
        self.lst_user_type.insert(tkinter.END, 'A')
        self.lst_user_type.insert(tkinter.END, 'B')
        self.lst_user_type.pack(expand=True, fill="none", padx=10, pady=10)

        btn_add_user = tkinter.ttk.Button(self.frame_add_employees_dop, text=_("Add Employee"), \
                                          command=self.add_user_db)
        btn_add_user.pack(expand=True, fill="none", padx=10, pady=10)

    def add_user_db(self):
        """add_user_db."""
        """TODO: занести в базу данных всю информацию о новом работяге, проверить корректность введенных данных"""
        vr_user_name = self.vr_user_name.get()
        vr_user_password = self.vr_user_password.get()
        lst_user_type = 'AB'[self.lst_user_type.curselection()[0]]
        try:
            conn = psycopg2.connect("dbname = 'db_user' user = 'postgres' host='localhost' password='0852'")
        except Exception as e:
            print(f'Undefined error {e}')

        with conn.cursor() as curs:
            curs.execute('SELECT user_name FROM user_authorization')
            q = list(map(lambda x: x[0], curs.fetchall()))
            if vr_user_name in q:
                mb.showerror("Error!", "Name already exist!")
            else:
                curs.execute("SELECT user_id FROM user_type")
                counter = 0
                flag = True
                for i in sorted(curs.fetchall()):
                    if i[0] != counter:
                        vr_user_fid = counter
                        flag = False
                        break
                    counter += 1
                if flag:
                    vr_user_fid = counter

                curs.execute("SELECT user_id FROM user_authorization")
                counter = 0
                flag = True
                for i in sorted(curs.fetchall()):
                    if i[0] != counter:
                        vr_user_id = counter
                        flag = False
                        break
                    counter += 1
                if flag:
                    vr_user_id = counter

                curs.execute(f"""
                    INSERT INTO user_type (user_id,user_type) VALUES ({vr_user_fid},'{lst_user_type}');
                    COMMIT
                    """)

                curs.execute(f"""
                    INSERT INTO user_authorization (user_id,user_fid,user_name,user_password) VALUES ({vr_user_id},
                        {vr_user_fid},'{vr_user_name}','{vr_user_password}');
                    COMMIT
                    """)

                # после этого выполняется следующий блок код

                self.update_foo()

    def widgets_del_employees(self):
        """widgets_employees."""
        lbl_user_id = tkinter.ttk.Label(self.frame_del_employees_dop, text=_('Employee ID'), font=('Arial', 16))

        self.vr_user_id = tkinter.StringVar()

        lbl_user_id.pack(expand=True, fill="none", padx=10, pady=10)
        ntr_user_id = tkinter.ttk.Entry(self.frame_del_employees_dop, textvariable=self.vr_user_id)
        ntr_user_id.pack(expand=True, fill="none", padx=10, pady=10)

        btn_del_user = tkinter.ttk.Button(self.frame_del_employees_dop, text=_("Delete Employee"), \
                                          command=self.del_user_db)
        btn_del_user.pack(expand=True, fill="none", padx=10, pady=10)

    def del_user_db(self):
        """del_user_db."""
        """TODO: удалить из базы данных всю информацию о пользователе (и в задачах тоже (кто коммитил оставить)),
        проверить корректность введенных данных"""
        vr_user_id = self.vr_user_id.get()
        try:
            conn = psycopg2.connect("dbname = 'db_user' user = 'postgres' host='localhost' password='0852'")
        except Exception as e:
            print(f'Undefined error {e}')

        with conn.cursor() as curs:
            curs.execute('SELECT user_id FROM user_authorization')
            q = list(map(lambda x: x[0], curs.fetchall()))
            if int(vr_user_id) not in q:
                mb.showerror("Error!", f"User with ID {vr_user_id} doesnt exist")
            else:
                curs.execute(f"""
                    SELECT user_id,user_fid FROM user_authorization
                    WHERE user_id = {vr_user_id}
                """)
                q = curs.fetchone()
                curs.execute(f"""
                    DELETE FROM user_authorization
                    WHERE user_id = {q[0]};
                    COMMIT
                    """)

                curs.execute(f"""
                    DELETE FROM user_type
                    WHERE user_id = {q[1]};
                    COMMIT
                    """)

                try:
                    conn = psycopg2.connect("dbname = 'db_task' user = 'postgres' host='localhost' password='0852'")
                except Exception as e:
                    print(f'Undefined error {e}')

                with conn.cursor() as curs:
                    curs.execute("""
                        SELECT task_id,task_workers FROM task_info
                        """)
                    w = curs.fetchall()
                    for i in w:
                        if q[0] in i[1]:
                            new_list = list(i[1])
                            new_list.pop(new_list.index(q[0]))
                            curs.execute(f"""
                                UPDATE task_info
                                SET task_workers = {new_list}
                                WHERE task_id = {i[0]};
                                COMMIT
                                """)

                # после этого выполняется следующий блок код

                self.update_foo()

    def widgets_add_task(self):
        """widgets_task."""

        def on_enter_press(event):
            """on_enter_press.

            :param event:
            """
            self.txt_task_description.insert(tkinter.END, '\n')
            self.txt_task_description.see(tkinter.END)

        lbl_task_name = tkinter.ttk.Label(self.frame_add_task_dop, text=_('Task Name'), font=('Arial', 16))
        lbl_task_supervisor = tkinter.ttk.Label(self.frame_add_task_dop, text=_('Task Supervisor'), font=('Arial', 16))
        lbl_task_workers = tkinter.ttk.Label(self.frame_add_task_dop, text=_('Task Workers'), font=('Arial', 16))
        lbl_task_description = tkinter.ttk.Label(self.frame_add_task_dop, text=_('Description'), font=('Arial', 16))
        lbl_task_deadline = tkinter.ttk.Label(self.frame_add_task_dop, text=_('Deadline'), font=('Arial', 16))

        self.vr_task_name = tkinter.StringVar()
        self.vr_task_supervisor = tkinter.StringVar()
        self.vr_task_workers = tkinter.StringVar()
        self.vr_task_workers.set(_("Enter ID separated by space"))
        self.vr_task_deadline = tkinter.StringVar()

        lbl_task_name.pack(expand=True, fill="none", padx=10, pady=10)
        ntr_task_name = tkinter.ttk.Entry(self.frame_add_task_dop, textvariable=self.vr_task_name)
        ntr_task_name.pack(expand=True, fill="none", padx=10, pady=10)

        lbl_task_supervisor.pack(expand=True, fill="none", padx=10, pady=10)
        ntr_task_supervisor = tkinter.ttk.Entry(self.frame_add_task_dop, textvariable=self.vr_task_supervisor)
        ntr_task_supervisor.pack(expand=True, fill="none", padx=10, pady=10)

        lbl_task_workers.pack(expand=True, fill="none", padx=10, pady=10)
        ntr_task_workers = tkinter.ttk.Entry(self.frame_add_task_dop, textvariable=self.vr_task_workers)
        ntr_task_workers.pack(expand=True, fill="none", padx=10, pady=10)

        lbl_task_description.pack(expand=True, fill="none", padx=10, pady=10)
        self.txt_task_description = tkinter.Text(self.frame_add_task_dop, wrap='word', height=10, width=40)
        self.txt_task_description.pack(expand=True, fill="both", padx=10, pady=10)
        self.txt_task_description.bind('<Return>', on_enter_press)

        lbl_task_deadline.pack(expand=True, fill="none", padx=10, pady=10)
        ntr_task_deadline = tkinter.ttk.Entry(self.frame_add_task_dop, textvariable=self.vr_task_deadline)
        ntr_task_deadline.pack(expand=True, fill="none", padx=10, pady=10)

        btn_add_task = tkinter.ttk.Button(self.frame_add_task_dop, text=_("Add Task"), \
                                          command=self.add_task_db)
        btn_add_task.pack(expand=True, fill="none", padx=10, pady=10)

    def add_task_db(self):
        """add_task_db."""
        """TODO: занести в базу данных всю информацию о новой задаче, проверить корректность введенных данных"""
        vr_task_name = self.vr_task_name.get()
        vr_task_supervisor = self.vr_task_supervisor.get()
        vr_task_workers = list(map(int, self.vr_task_workers.get().split()))
        vr_task_deadline = self.vr_task_deadline.get()
        day, month, year = vr_task_deadline.split('.')
        vr_task_descr = self.txt_task_description.get('1.0', tkinter.END)
        flag_supervisor = False
        flag_user = False
        flag_can_be_supervisor = False

        try:
            conn = psycopg2.connect("dbname = 'db_user' user = 'postgres' host='localhost' password='0852'")
        except Exception as e:
            print(f'Undefined error {e}')
        with conn.cursor() as curs:
            curs.execute("SELECT user_id FROM user_authorization")
            q = list(map(lambda x: x[0], curs.fetchall()))
            if int(vr_task_supervisor) not in q:
                flag_supervisor = True
            for i in vr_task_workers:
                if i not in q:
                    flag_user = True
                    break
            if not flag_supervisor:
                curs.execute(f"""
                    SELECT user_fid FROM user_authorization
                    WHERE user_id = {vr_task_supervisor}
                    """)
                q = curs.fetchone()[0]
                curs.execute(f"""
                    SELECT * FROM user_type
                    WHERE user_id = {q}
                    """)
                q = curs.fetchone()
                flag_can_be_supervisor = q[1] == 'B'
        try:
            conn = psycopg2.connect("dbname = 'db_task' user = 'postgres' host='localhost' password='0852'")
        except Exception as e:
            print(f'Undefined error {e}')

        with conn.cursor() as curs:
            curs.execute("SELECT task_name FROM task_info")
            q = list(map(lambda x: x[0], curs.fetchall()))
            if vr_task_name in q:
                mb.showerror("Error!", f"Task with name {vr_task_name} already exist")
            elif flag_supervisor:
                mb.showerror("Error!", f"User with ID {vr_task_supervisor} doesnt exist")
            elif flag_can_be_supervisor:
                mb.showerror("Error!", "This user doesnt have enough permission")
            elif flag_user:
                mb.showerror("Error!", "Incorrect list of users")
            elif datetime(day=int(day), month=int(month), year=int(year)) < datetime.now():
                mb.showerror("Error!", "Incorrect deadline time")
            else:
                curs.execute("SELECT task_id FROM task_info")
                counter = 0
                flag = True
                for i in sorted(curs.fetchall()):
                    if i[0] != counter:
                        vr_task_id = counter
                        flag = False
                        break
                    counter += 1
                if flag:
                    vr_task_id = counter
                curs.execute(f"""
                    INSERT INTO task_info (task_id,task_name,task_supervisor,task_workers,percent,deadline,description)
                    VALUES ({vr_task_id},'{vr_task_name}',{vr_task_supervisor},ARRAY{vr_task_workers},0,
                    '{year}-{month}-{day}','{vr_task_descr}');
                    COMMIT
                    """)

                # после этого выполняется следующий блок код

                self.update_foo()

    def widgets_del_task(self):
        """widgets_task."""
        lbl_task_id = tkinter.ttk.Label(self.frame_del_task_dop, text=_('Task ID'), font=('Arial', 16))

        self.vr_del_task_id = tkinter.StringVar()

        lbl_task_id.pack(expand=True, fill="none", padx=10, pady=10)
        ntr_task_id = tkinter.ttk.Entry(self.frame_del_task_dop, textvariable=self.vr_del_task_id)
        ntr_task_id.pack(expand=True, fill="none", padx=10, pady=10)

        btn_del_task = tkinter.ttk.Button(self.frame_del_task_dop, text=_("Delete Task"), \
                                          command=self.del_task_db)
        btn_del_task.pack(expand=True, fill="none", padx=10, pady=10)

    def del_task_db(self):
        """del_task_db."""
        """TODO: удалить из базы данных всю информацию о задаче, проверить корректность введенных данных"""

        vr_del_task_id = self.vr_del_task_id.get()
        try:
            conn = psycopg2.connect("dbname = 'db_task' user = 'postgres' host='localhost' password='0852'")
        except Exception as e:
            print(f'Undefined error {e}')

        with conn.cursor() as curs:
            curs.execute("SELECT task_id FROM task_info")
            q = list(map(lambda x: x[0], curs.fetchall()))
            if int(vr_del_task_id) not in q:
                mb.showerror("Error!", f"Task with ID {vr_del_task_id} doesnt exist")
            else:
                curs.execute(f"""
                    DELETE FROM task_entry
                    WHERE task_id = {vr_del_task_id};
                    COMMIT
                    """)

                curs.execute(f"""
                    DELETE FROM task_info
                    WHERE task_id = {vr_del_task_id};
                    COMMIT
                    """)

                # после этого выполняется следующий блок код

                self.update_foo()


def pre_main():
    """pre_main."""
    """ TODO: авторизация, проверка user_name, user_password
    и добавление в user_type его тип 'B' -- zavod, 'A' иначе """
    global user_type, worker_id

    if len(sys.argv) != 1 and len(sys.argv) != 3:
        print('Incorrect positional arguments')
    else:
        if len(sys.argv) == 1:
            print('Using superuser mode')
            user = 'admin'
            password = 'admin'
        else:
            user = sys.argv[1]
            password = sys.argv[2]
        try:
            conn = psycopg2.connect("dbname = 'db_user' user = 'postgres' host='localhost' password='0852'")
        except Exception as e:
            print(f'Undefined error {e}')

        with conn.cursor() as curs:
            curs.execute(f"""
                SELECT * FROM user_authorization
                WHERE user_name = '{user}'
                """)
            person = curs.fetchone()
            if not person:
                print('Unknown user')
            else:
                if person[3] != password:
                    print('Incorrect password. Try again')
                else:
                    curs.execute(f"""
                        SELECT * FROM user_type
                        WHERE user_id = {person[1]}
                        """)
                    user_type = curs.fetchone()[1]
                    worker_id = person[0]
                    root = tkinter.Tk()
                    root.geometry("1280x720")
                    Application(root)
                    root.mainloop()
