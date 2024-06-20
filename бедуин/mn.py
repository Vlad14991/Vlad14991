import tkinter as tk
from tkinter import messagebox, simpledialog
from plyer import notification

class BedouinWaterApp:
    def __init__(self, master):
        self.master = master
        master.title("Приложение контроля питьевого режима 'Бедуин'")
        master.geometry("451x405")

        self.weight = tk.DoubleVar(value=0)
        self.glass_volume = tk.IntVar(value=250)
        self.water_goal_ml = 0
        self.water_count = 0
        self.notification_id = None

        self.load_settings()
        self.create_widgets()
        self.reminder()

    def remaining_water(self):
        return max(self.water_goal_ml - self.water_count, 0)

    def drink_water(self):
        if self.weight.get() == 0:
            messagebox.showerror("Ошибка", "Пожалуйста, сначала установите свой вес.")
            return

        remaining = self.remaining_water()
        if remaining > 0:
            self.water_count += self.glass_volume.get()
            self.label_count.config(text=f"Выпито воды: {self.water_count} мл")
            self.update_progress()
            self.update_glasses_count()
            messagebox.showinfo("Осталось выпить", f"Осталось выпить: {remaining} мл")
        else:
            messagebox.showinfo("Поздравляем!", "Вы выпили рекомендуемое количество воды на сегодня!")
            self.reminder()

    def load_settings(self):
        try:
            with open("bedouin_settings.txt", "r") as file:
                self.weight.set(float(file.readline()))
                self.glass_volume.set(int(file.readline()))
        except FileNotFoundError:
            pass

    def save_settings(self):
        with open("bedouin_settings.txt", "w") as file:
            file.write(f"{self.weight.get()}\n{self.glass_volume.get()}\n")

    def create_widgets(self):
        tk.Label(self.master, text="Введите свой вес (кг) и объем стакана (мл):", font=("Arial", 10)).pack(pady=5)

        self.entry_weight = tk.Entry(self.master, textvariable=self.weight, font=("Arial", 10))
        self.entry_weight.pack(pady=5)

        self.entry_glass = tk.Entry(self.master, textvariable=self.glass_volume, font=("Arial", 10))
        self.entry_glass.pack(pady=5)

        tk.Button(self.master, text="Установить вес и стакан", command=self.set_weight_and_glass, font=("Arial", 10)).pack(pady=5)

        self.label_count = tk.Label(self.master, text="Выпито воды: 0 мл", font=("Arial", 10))
        self.label_count.pack(pady=5)

        self.label_goal = tk.Label(self.master, text=f"Рекомендуемое количество воды в день: {self.water_goal_ml} мл", font=("Arial", 10))
        self.label_goal.pack(pady=5)

        self.label_glasses = tk.Label(self.master, text=f"Количество стаканов для выпивания: {self.water_goal_ml // self.glass_volume.get()}", font=("Arial", 10))
        self.label_glasses.pack(pady=5)

        tk.Label(self.master, text="Прогресс:", font=("Arial", 10)).pack(pady=5)

        self.progress_percent = tk.Label(self.master, text="0%", font=("Arial", 10))
        self.progress_percent.pack(pady=5)

        self.progress_bar = tk.Canvas(self.master, width=200, height=20, bg='lightgray', relief='raised')
        self.progress_bar.pack()

        tk.Button(self.master, text="Пить", command=self.drink_water, font=("Arial", 10)).pack(pady=10)
        tk.Button(self.master, text="Настройка цели", command=self.set_goal, font=("Arial", 10)).pack(pady=5)

    def set_weight_and_glass(self):
        try:
            self.save_settings()
            self.water_goal_ml = int(self.weight.get() * 30)
            self.update_goal()
            self.update_glasses_count()
        except ValueError:
            messagebox.showerror("Ошибка", "Пожалуйста, введите числовое значение веса и объема стакана.")

    def update_goal(self):
        self.label_goal.config(text=f"Рекомендуемое количество воды в день: {self.water_goal_ml} мл")

    def update_progress(self):
        progress_percent = min((self.water_count / self.water_goal_ml) * 100, 100)
        self.progress_percent.config(text=f"{progress_percent:.1f}%")
        self.progress_bar.delete("progress")
        self.progress_bar.create_rectangle(0, 0, progress_percent * 2, 20, fill='blue', tags="progress")

    def set_goal(self):
        if self.weight.get() == 0:
            messagebox.showerror("Ошибка", "Пожалуйста, сначала установите свой вес и объем стакана.")
            return
        new_goal = simpledialog.askinteger("Настройка цели", "Введите новое количество воды в миллилитрах:")
        if new_goal is not None:
            self.water_goal_ml = new_goal
            self.update_progress()
            self.update_glasses_count()

    def update_glasses_count(self):
        glasses_count = self.water_goal_ml // self.glass_volume.get()
        self.label_glasses.config(text=f"Количество стаканов для выпивания: {glasses_count}")

    def reminder(self):
        if self.weight.get() == 0:
            return
        if self.water_count < self.water_goal_ml:
            if self.notification_id is None:
                self.notification_id = notification.notify(
                    title="Напоминание",
                    message="Не забудьте выпить воду!",
                    timeout=2
                )

            self.master.after(20000, self.reminder)
        else:
            if self.notification_id is not None:
                notification.stop(self.notification_id)
                self.notification_id = None
            self.master.after(20000, self.reminder)

root = tk.Tk()
app = BedouinWaterApp(root)
root.mainloop()
