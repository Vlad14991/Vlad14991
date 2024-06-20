import random

Gamer_HP_SL = 100
Gamer_HP_SR = 100

for i in range(100):
    print('Выберите действие 1-Атака 2-Защита')
    b = int(input('Первый игрок (1-Атака, 2-Защита): '))
    f = int(input('Второй игрок (1-Атака, 2-Защита): '))

    if b == 2 and f == 1:
        B = random.randint(1, 15)
        if B >= 5:
            print('Первый игрок: Защита прошла')
        else:
            A = random.randint(5, 11)
            Gamer_HP_SR -= A
            print('Первый игрок: Защита не прошла')
            print('Здоровье первого игрока =', Gamer_HP_SR)

    if b == 1 and f == 1:
        A = random.randint(5, 11)
        Gamer_HP_SR -= A
        print('Здоровье первого игрока =', Gamer_HP_SR)
        a = random.randint(5, 11)
        Gamer_HP_SL -= a
        print('Здоровье второго игрока =', Gamer_HP_SL)

    if f == 2 and b == 1:
        c = random.randint(1, 15)
        if c >= 5:
            print('Второй игрок: Защита прошла')
        else:
            A = random.randint(5, 11)
            Gamer_HP_SL -= A
            print('Второй игрок: Защита не прошла')
            print('Здоровье второго игрока =', Gamer_HP_SL)

    if b == 2 and f == 2:
        print('Пропуск хода')

    if Gamer_HP_SR <= 0 and Gamer_HP_SL <= 0:
        print('Погибли все)')
        break
    if Gamer_HP_SL <= 0 and Gamer_HP_SR > 0:
        print('Первый игрок победил')
        break
    if Gamer_HP_SR <= 0 and Gamer_HP_SL > 0:
        print('Второй игрок победил')
        break
