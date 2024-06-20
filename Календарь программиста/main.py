import tkinter as tk
from tkinter import messagebox, simpledialog

class ProgrammerCalendarApp:
    def __init__(self, master):
        self.master = master
        master.title("Настоящее Кунг-фу: Календарь программиста")
        master.geometry("600x400")
        master.configure(bg="#f0f0f0")  # устанавливаем цвет фона

        self.events = []

        self.create_widgets()

    def create_widgets(self):
        self.label_title = tk.Label(self.master, text="Настоящее Кунг-фу: Календарь программиста", font=("Arial", 14), bg="#f0f0f0")
        self.label_title.pack(pady=10)

        self.button_add_event = tk.Button(self.master, text="Добавить событие", command=self.add_event, bg="#4CAF50", fg="white", padx=10, pady=5)
        self.button_add_event.pack(pady=5)

        self.button_view_tasks = tk.Button(self.master, text="Просмотреть задачи на день", command=self.view_tasks, bg="#008CBA", fg="white", padx=10, pady=5)
        self.button_view_tasks.pack(pady=5)

        self.listbox_events = tk.Listbox(self.master, width=50, height=15)
        self.listbox_events.pack(pady=10)

    def add_event(self):
        date = simpledialog.askstring("Добавление события", "Введите дату события (ГГГГ-ММ-ДД):")
        time = simpledialog.askstring("Добавление события", "Введите время события (ЧЧ:ММ):")
        description = simpledialog.askstring("Добавление события", "Введите описание события:")

        event = {"date": date, "time": time, "description": description}
        self.events.append(event)
        self.update_event_list()
        messagebox.showinfo("Событие добавлено", "Событие успешно добавлено в календарь.")

    def view_tasks(self):
        date = simpledialog.askstring("Просмотр задач на день", "Введите дату для просмотра задач (ГГГГ-ММ-ДД):")
        tasks = [event for event in self.events if event["date"] == date]
        if tasks:
            task_list = "\n".join([f"{task['time']} - {task['description']}" for task in tasks])
            messagebox.showinfo("Задачи на день", f"Задачи на {date}:\n{task_list}")
        else:
            messagebox.showinfo("Задачи на день", f"На {date} задач нет.")

    def update_event_list(self):
        self.listbox_events.delete(0, tk.END)
        for event in self.events:
            self.listbox_events.insert(tk.END, f"{event['date']} {event['time']} - {event['description']}")

root = tk.Tk()
app = ProgrammerCalendarApp(root)
root.mainloop()
