def month_to_season(m):
    if m < 1 or m > 12:
        print("Такого месяца не существует")
    elif (m == 12 or m < 3):
        print("Зима")
    elif (5 >= m >= 3):
        print("Весна")
    elif (8 >= m >=6):
        print("Лето")
    else: 
        print("Осень")
        
month_number = int(input("Введите номер месяца: "))

month_to_season(month_number)
