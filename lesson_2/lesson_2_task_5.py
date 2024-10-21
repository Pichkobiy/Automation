def month_to_season(moth):
    if moth in[1, 2, 12]:
        print("Зима")
    elif moth in[3, 4, 5]:
        print("Весна")
    elif moth in[6, 7, 8]:
        print("Лето")
    elif moth in[9, 10, 11]:
        print("Осень")
    else:
        print("Введите число от 1 до 12")

month_to_season(8)
