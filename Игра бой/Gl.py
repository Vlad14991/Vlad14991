import os
from random import randint


class Player:
  hp = 100
  damage = 10
  wins = 0
  fol = 0


p = Player()


class Enemy:

  hp = randint(70, 150)
  damage = randint(10, 15)


def menu(p):
  while True:
    print("""1) Сражаться 2) Статистика""")
    try:
      n = input("Введите число: ")

      if int(n) == 1:
        menu_fight(p)
      if int(n) == 2:
        menu_stats(p)
      else:
        print("Чего ждем?")

    except NameError:
      ...
    except SyntaxError:
      ...
    except ValueError:
      ...


def menu_stats(p):
  os.system("cls||clear")
  print("Статистика игрока")
  print("*****************")
  print(f"""
побед: {p.wins}
поражений: {p.fol}
""")


def menu_fight(p):
  p.hp = 100
  e = Enemy()
  os.system("cls||clear")

  print(f"Вы hp: {p.hp} damage: {p.damage}")
  print(f"Враг hp: {e.hp} damage: {e.damage}")
  print("**********************")
  while e.hp > 0:
    # Также, как я и сказал по последовательности списка расставляет переменные.
    print("1)Ударить")
    print("2)Хил 5-15")
    n = input("Введите число: ")
    if int(n) == 1:
      os.system("cls||clear")

      # Здоровье врага отнимает от вашего дамага.
      e.hp -= p.damage
      print(f"Вы ударили противника, у него осталось {e.hp} hp")
      # Здоровье игрока отнимает от дамага врага.
      p.hp -= e.damage
      print(f"Противник ударил вас, у вас осталось {p.hp} hp")

      print("*********************")

    elif int(n) == 2:
      os.system("cls||clear")
      # Рандомно от 5 до 15 добавляет хп.
      p.hp += randint(5, 15)
      # Если здоровье игрока больше, то хп игрока будет равна 100.
      if p.hp > 100:
        p.hp = 100

      print(f"Ваши хп {p.hp}")

    else:
      print("Чего ждем?")
    if p.hp < 0:
      os.system("cls||clear")
      print("Вы проиграли")
      p.fol += 1
      brake
    if e.hp < 0:
      os.system("cls||clear")
      print("Вы победили")
      p.wins += 1
      brake
menu(p)