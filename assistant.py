import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3 as sql

class ToDoListManager:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("To-Do List Manager - ARSHAD")
        self.root.geometry("500x450+750+250")
        self.root.resizable(0, 0)
        self.root.configure(bg="#FAEBD7")

        self.db_connection = sql.connect('listofTasks.db')
        self.db_cursor = self.db_connection.cursor()
        self.db_cursor.execute('create table if not exists tasks (title text)')

        self.tasks = []

        self.header_frame = tk.Frame(self.root, bg="#8B4513")  # SaddleBrown
        self.functions_frame = tk.Frame(self.root, bg="#8B4513")  # SaddleBrown
        self.listbox_frame = tk.Frame(self.root, bg="#8B4513")  # SaddleBrown

        self.header_frame.pack(fill="both")
        self.functions_frame.pack(side="left", expand=True, fill="both")
        self.listbox_frame.pack(side="right", expand=True, fill="both")

        self.header_label = ttk.Label(
            self.header_frame,
            text="To-Do List",
            font=("Alice", "30", "bold"),
            background="#8B4513",  # SaddleBrown
            foreground="#FFFFFF"
        )
        self.header_label.pack(padx=10, pady=10)

        self.task_label = ttk.Label(
            self.functions_frame,
            text="Enter the Task:",
            font=("Alice", "11", "bold"),
            background="#8B4513",  # SaddleBrown
            foreground="#FFFFFF"
        )
        self.task_label.place(x=30, y=40)
        self.task_field = ttk.Entry(
            self.functions_frame,
            font=("Consolas", "12"),
            width=18,
            background="#8B4513",  # SaddleBrown
            foreground="#A52A2A"  # Brown
        )
        self.task_field.place(x=30, y=80)

        self.add_button = ttk.Button(
            self.functions_frame,
            text="Add Task",
            width=24,
            command=self.add_task,
            style="Custom.TButton"
        )
        self.del_button = ttk.Button(
            self.functions_frame,
            text="Delete Task",
            width=24,
            command=self.delete_task,
            style="Custom.TButton"
        )
        self.del_all_button = ttk.Button(
            self.functions_frame,
            text="Delete All Tasks",
            width=24,
            command=self.delete_all_tasks,
            style="Custom.TButton"
        )
        self.exit_button = ttk.Button(
            self.functions_frame,
            text="Exit",
            width=24,
            command=self.close,
            style="Custom.TButton"
        )
        self.add_button.place(x=30, y=120)
        self.del_button.place(x=30, y=160)
        self.del_all_button.place(x=30, y=200)
        self.exit_button.place(x=30, y=240)

        self.task_listbox = tk.Listbox(
            self.listbox_frame,
            width=26,
            height=13,
            selectmode='SINGLE',
            background="#FFFFFF",
            foreground="#000000",
            selectbackground="#CD853F",
            selectforeground="#FFFFFF"
        )
        self.task_listbox.place(x=10, y=20)

        self.retrieve_database()
        self.list_update()

    def add_task(self):
        task_string = self.task_field.get()
        if not task_string:
            messagebox.showinfo('Error', 'Field is empty.')
            return
        self.tasks.append(task_string)
        self.db_cursor.execute('insert into tasks (title) values (?)', (task_string,))
        self.list_update()
        self.task_field.delete(0, 'end')

    def list_update(self):
        self.clear_list()
        for task in self.tasks:
            self.task_listbox.insert('end', task)

    def delete_task(self):
        try:
            task_value = self.task_listbox.get(self.task_listbox.curselection())
            if task_value in self.tasks:
                self.tasks.remove(task_value)
                self.list_update()
                self.db_cursor.execute('delete from tasks where title =?', (task_value,))
        except:
            messagebox.showinfo('Error', 'No Task Selected. Cannot Delete')

    def delete_all_tasks(self):
        if messagebox.askyesno('Delete All', 'Are You Sure?'):
            while len(self.tasks)!= 0:
                self.tasks.pop()
            self.db_cursor.execute('delete from tasks')
            self.list_update()

    def clear_list(self):
        self.task_listbox.delete(0, 'end')

    def close(self):
        print(self.tasks)
        self.db_connection.commit()
        self.db_cursor.close()
        self.root.destroy()

    def retrieve_database(self):
        while len(self.tasks)!= 0:
            self.tasks.pop()
        for row in self.db_cursor.execute('select title from tasks'):
            self.tasks.append(row[0])

if __name__ == "__main__":
    root = tk.Tk()
    style = ttk.Style(root)
    style.configure("Custom.TButton", background="#CD853F", foreground="#FFFFFF", font=("Arial", 10, "bold"))
    app = ToDoListManager(root)
    root.mainloop()
