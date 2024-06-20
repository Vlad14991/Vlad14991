import random

class FoodTerminal:
    def __init__(self):
        self.menu = {
            'Добрый Кола 0,65 мл. 🥤': 80,
            'Добрый Апельсин 0,65 мл. 🥤': 80,
            'Шашлык куриный 250 гр. 🍗': 240,
            'Шаурма MIX курица x говядина 413 гр. 🌯': 280,
            'Салатик Греческий 320 гр. 🥗': 180,
        }
        self.shopping_cart = []

    def display_menu(self):
        print("\nМеню:")
        for index, (item, price) in enumerate(self.menu.items(), start=1):
            print(f"{index}. {item}: {price} р.")

    def take_order(self):
        self.display_menu()
        order_choice = input("Введите номера блюд, которые вы хотите заказать (разделяйте запятыми): ")
        order_indices = [int(i.strip()) for i in order_choice.split(',')]
        for index in order_indices:
            if 1 <= index <= len(self.menu):
                item, price = list(self.menu.items())[index - 1]
                self.shopping_cart.append((item, price))
            else:
                print(f"Ошибка: 404 не найдено {index}.")

    def view_shopping_cart(self):
        if not self.shopping_cart:
            print("Ваша корзина пуста.")
        else:
            print("Корзина покупок:")
            for item, price in self.shopping_cart:
                print(f"{item}: {price} р.")

    def checkout(self):
        self.view_shopping_cart()
        if not self.shopping_cart:
            print("Ваш заказ пуст. Пожалуйста, добавьте блюда в корзину перед оплатой.")
            return
        total_cost = sum(price for _, price in self.shopping_cart)
        print(f"\nИтоговая стоимость заказа: {total_cost:.2f} р.")
        payment_method = input("Выберите метод оплаты (1 - Наличные, 2 - Карта): ")
        if payment_method == '1':
            while True:
                try:
                    payment_amount = float(input("Введите сумму оплаты наличными: "))
                    if payment_amount >= total_cost:
                        change = payment_amount - total_cost
                        order_number = random.randint(1, 2000)
                        print(f"Оплата прошла успешно. Спасибо за покупку! Ваша сдача: {change:.2f} р.")
                        print(f"Номер вашего заказа: {order_number}")
                        self.shopping_cart = []
                        break
                    else:
                        print("Недостаточно средств для оплаты заказа.")
                except ValueError:
                    print("Введите корректную сумму.")
        elif payment_method == '2':
            order_number = random.randint(1, 2000)
            print("Оплата картой прошла успешно. Спасибо за покупку!")
            print(f"Номер вашего заказа: {order_number}")
            self.shopping_cart = []
        else:
            print("Неверный метод оплаты. Пожалуйста, введите 1 или 2.")

if __name__ == "__main__":
    terminal = FoodTerminal()

    while True:
        print('●▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬●')
        print('  ▀▄▀▄▀▄ ДОБРО ПОЖАЛОВАТЬ ▄▀▄▀▄▀')
        print('●▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬●')
        print("\nИнформационный терминал пищеблок:")
        print("[1] - Меню")
        print("[2] - Выбор блюд и напитков")
        print("[3] - Посмотреть корзину покупок")
        print("[4] - Оплатить заказ")
        print("[5] - Выйти")
        print('         пїЏпїћгЂЂ гѓ•')
        print('гЂЂгЂЂгЂЂгЂЂгЂЂ| гЂЂ_гЂЂ _|')
        print('гЂЂ гЂЂгЂЂгЂЂпїЏ`гѓџ _x еЅЎ')
        print('гЂЂгЂЂгЂЂ /гЂЂгЂЂгЂЂ гЂЂ |')
        print('гЂЂгЂЂгЂЂ /гЂЂ гѓЅгЂЂгЂЂ пѕ‰')
        print('гЂЂпїЏпїЈ|гЂЂгЂЂ |гЂЂ|гЂЂ|')
        print('гЂЂ| (пїЈгѓЅпїї_гѓЅ_)_)')
        print('гЂЂпїјдєЊгЃ¤')

        choice = input("Введите номер: ")
        if choice == '1':
            terminal.display_menu()
        elif choice == '2':
            terminal.take_order()
        elif choice == '3':
            terminal.view_shopping_cart()
        elif choice == '4':
            terminal.checkout()
        elif choice == '5':
            print("Спасибо за покупку! Приходите ещё.")
            break
        else:
            print("Неверный выбор. Пожалуйста, введите 1, 2, 3, 4 или 5.")
