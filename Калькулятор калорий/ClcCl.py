import tkinter as tk
from tkinter import messagebox

class CalorieCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calorie Calculator")
        root.geometry("300x400")
        self.food_items = {}
        self.activity_levels = {"Сидячий": 1.2, "Легкая активность": 1.375, "Умеренная активность": 1.55, "Высокая активность": 1.725, "Очень высокая активность": 1.9}

        self.weight_label = tk.Label(root, text="Вес (кг):")
        self.weight_label.pack()

        self.weight_entry = tk.Entry(root)
        self.weight_entry.pack()

        self.height_label = tk.Label(root, text="Рост (см):")
        self.height_label.pack()

        self.height_entry = tk.Entry(root)
        self.height_entry.pack()

        self.age_label = tk.Label(root, text="Возраст:")
        self.age_label.pack()

        self.age_entry = tk.Entry(root)
        self.age_entry.pack()

        self.activity_label = tk.Label(root, text="Уровень активности:")
        self.activity_label.pack()

        self.activity_var = tk.StringVar(root)
        self.activity_var.set("Сидячий")  # Default value
        self.activity_menu = tk.OptionMenu(root, self.activity_var, *self.activity_levels.keys())
        self.activity_menu.pack()

        self.food_label = tk.Label(root, text="Продукт:")
        self.food_label.pack()

        self.food_entry = tk.Entry(root)
        self.food_entry.pack()

        self.calories_label = tk.Label(root, text="Калории:")
        self.calories_label.pack()

        self.calories_entry = tk.Entry(root)
        self.calories_entry.pack()

        self.add_button = tk.Button(root, text="Добавить продукт", command=self.add_food_item)
        self.add_button.pack()

        self.calculate_button = tk.Button(root, text="Рассчитать калории", command=self.calculate_calories)
        self.calculate_button.pack()

    def add_food_item(self):
        food = self.food_entry.get()
        calories = self.calories_entry.get()
        if food and calories:
            try:
                self.food_items[food] = int(calories)
                messagebox.showinfo("Успех", "Продукт добавлен")
                self.food_entry.delete(0, tk.END)
                self.calories_entry.delete(0, tk.END)
            except ValueError:
                messagebox.showerror("Ошибка", "Введите корректное значение калорий")
        else:
            messagebox.showerror("Ошибка", "Введите название продукта и калорийность")

    def calculate_calories(self):
        try:
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get())
            age = int(self.age_entry.get())
            activity_factor = self.activity_levels[self.activity_var.get()]

            bmr = 10 * weight + 6.25 * height - 5 * age + 5  # Mifflin-St Jeor Equation for men
            tdee = bmr * activity_factor

            total_food_calories = sum(self.food_items.values())
            total_calories = tdee + total_food_calories
            messagebox.showinfo("Общее количество калорий", f"Общее количество калорий: {total_calories:.2f}")
        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректные значения для веса, роста и возраста")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalorieCalculatorApp(root)
    root.mainloop()
