import tkinter as tk
from tkinter import messagebox
import os

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")

        self.tasks = []
        self.file_name = "todo_list.txt"

        self.load_tasks()

        self.create_widgets()

    def create_widgets(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        self.task_listbox = tk.Listbox(self.frame, width=50, height=10, selectmode=tk.SINGLE)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        self.entry = tk.Entry(self.root, width=50)
        self.entry.pack(pady=10)

        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.complete_button = tk.Button(self.root, text="Mark as Complete", command=self.complete_task)
        self.complete_button.pack(pady=5)

        self.save_button = tk.Button(self.root, text="Save Tasks", command=self.save_tasks)
        self.save_button.pack(pady=5)

        self.load_tasks_into_listbox()

    def add_task(self):
        task = self.entry.get()
        if task != "":
            self.tasks.append((task, False))
            self.task_listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_task_index)
            del self.tasks[selected_task_index]
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def complete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            task, completed = self.tasks[selected_task_index]
            self.tasks[selected_task_index] = (task, not completed)
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to mark as complete.")

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task, completed in self.tasks:
            display_text = f"{task} - {'Completed' if completed else 'Not Completed'}"
            self.task_listbox.insert(tk.END, display_text)

    def save_tasks(self):
        with open(self.file_name, 'w') as file:
            for task, completed in self.tasks:
                file.write(f"{task}:::{completed}\n")

    def load_tasks(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, 'r') as file:
                for line in file:
                    task, completed = line.strip().split(":::")
                    self.tasks.append((task, completed == 'True'))

    def load_tasks_into_listbox(self):
        self.update_listbox()

    def on_closing(self):
        self.save_tasks()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()
