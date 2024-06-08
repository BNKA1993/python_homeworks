# # from user import User
# # from card import Card

# # alex = User("Alex")

# # alex.sayName()
# # alex.setAge(33)
# # alex.sayAge()

# # card = Card("1234 5678 8765 4321", "03/28", "Alex F")
# # alex.addCard(card)
# # alex.getCard().pay(1000)

# from turtle import *

# my_turtle = Turtle()
# my_turtle.speed(0)
# my_turtle.screen.setup(800, 800)


# def draw_oval(turtle, radius_horizontal, radius_vertical):
#     my_turtle.penup()
#     turtle.goto(0, -radius_vertical)
#     turtle.pendown()

#     for i in range(2):
#         turtle.circle(radius_horizontal, 90)
#         turtle.circle(radius_vertical, 90)

# # Настройка окна и черепашки
# window = turtle.Screen()
# window.bgcolor("white")

# # Создание черепашки
# oval_turtle = turtle.Turtle()
# oval_turtle.color("black")
# oval_turtle.speed(1)  # Вы можете изменить скорость рисования (1 - медленно, 10 - быстро, 0 - моментально)

# # Рисование овала
# draw_oval(oval_turtle, 100, 50)

# # Необходимо, чтобы окно не закрывалось само, а только по клику
# my_turtle.screen.exitonclick()
# # my_turtle.screen.mainloop()


def multiply_numbers_from_range(num1, num2):
    for i in range(num1, num2):
        i = num1
        multiply = 1
        while i <= num2:
            multiply = multiply * i
            i = i + 1
        return multiply
print(multiply_numbers_from_range(2, 4))