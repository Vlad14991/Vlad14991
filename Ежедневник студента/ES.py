import tkinter as tk
from tkinter import messagebox

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")
        root.geometry("300x400")
        self.tasks = {}

        self.date_label = tk.Label(root, text="Дата:")
        self.date_label.pack()

        self.date_entry = tk.Entry(root)
        self.date_entry.pack()

        self.task_label = tk.Label(root, text="Задача:")
        self.task_label.pack()

        self.task_entry = tk.Entry(root)
        self.task_entry.pack()

        self.priority_label = tk.Label(root, text="Приоритет:")
        self.priority_label.pack()

        self.priority_entry = tk.Entry(root)
        self.priority_entry.pack()

        self.add_button = tk.Button(root, text="Добавить задачу", command=self.add_task)
        self.add_button.pack()

        self.remove_button = tk.Button(root, text="Удалить задачу", command=self.remove_task)
        self.remove_button.pack()

        self.search_label = tk.Label(root, text="Поиск:")
        self.search_label.pack()

        self.search_entry = tk.Entry(root)
        self.search_entry.pack()

        self.search_button = tk.Button(root, text="Найти", command=self.search_task)
        self.search_button.pack()

    def add_task(self):
        date = self.date_entry.get()
        task = self.task_entry.get()
        priority = self.priority_entry.get()
        if date in self.tasks:
            self.tasks[date].append((task, priority))
        else:
            self.tasks[date] = [(task, priority)]
        messagebox.showinfo("Успех", "Задача добавлена")

    def remove_task(self):
        date = self.date_entry.get()
        task = self.task_entry.get()
        if date in self.tasks:
            for t, p in self.tasks[date]:
                if t == task:
                    self.tasks[date].remove((t, p))
                    if not self.tasks[date]:
                        del self.tasks[date]
                    messagebox.showinfo("Успех", "Задача удалена")
                    return
        messagebox.showerror("Ошибка", "Задача не найдена")

    def search_task(self):
        keyword = self.search_entry.get()
        results = []
        for date, tasks in self.tasks.items():
            for task, priority in tasks:
                if keyword.lower() in task.lower():
                    results.append((date, task, priority))
        if results:
            message = "Результаты поиска:\n"
            for date, task, priority in results:
                message += f"{date}: {task} (Приоритет: {priority})\n"
            messagebox.showinfo("Результаты поиска", message)
        else:
            messagebox.showinfo("Результаты поиска", "Ничего не найдено")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
