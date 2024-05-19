def bank(x,y):
    for i in range(y):
        x = x + (x * 10) / 100
    return x

x = int(input("Введите сумму: "))
y = int(input("Введите количество лет: "))


print("Итоговая сумма = ", round(bank(x,y)))