# ветвления

# age = 20
# if (age < 18):
#     print("Пейте сок")
# if (age > 18):
#     print("Можно не сок")



# password = "1234567890"
# if (password:= '1234567890'):
#     print("Успешная авторизация")
# else:
#     print("Неверный логин или пароль")



# rate_as_str = input("Оцените работу сотрудника от 1 до 5:")
# rate = int(rate_as_str)
# # print(rate)
# if (rate < 1):
#     rate = 1
# if (rate > 5):
#     rate = 5
# feedback = ''
# if rate == 1:
#     feedback = input("Расскажите, что нам улучшить: ")
# else: 
#     if rate == 2:
#         feedback = input("Расскажите, что вас смутило: ")
#     else: 
#         if rate == 3: 
#             feedback = input("Что именно пошло не так?")



# rate_as_str = input("Оцените работу сотрудника от 1 до 5:")
# rate = int(rate_as_str)
# # print(rate)
# if (rate < 1):
#     rate = 1
# if (rate > 5):
#     rate = 5

# feedback = ''

# if rate == 1:
#     feedback = input("Расскажите, что нам улучшить: ")
# elif rate ==2:
#     feedback = input("Расскажите, что вас смутило: ")
# elif rate ==3:
#     feedback = input("Расскажите, как нам стать лучше: ")
# elif rate ==4:
#     feedback = input("Почему не 5: ")
# else:
#     feedback = input("Расскажите, за что похвалить сотрудника: ")


#циклы

# for x in range(1, 10):
#     print(x)
    
# for x in range(1, 21):
#     print("x= ", x, "x²= ", x*x)

  
# students = ["Александр", "Михаил", "Мария"]
# l = len(students)  
# for y in range(0, l):
#     print(students[y])

# word = "Test"
# for spelling in word:
#     print(spelling)


# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for n in nums:
#     if (n%2 == 1):
#         print(n)
        
#логические операторы

# usel_login = "adam"
# user_password = "Qwerty123456"

# login = input("Login: ")
# password = input("Password: ")

# if login == usel_login and password == user_password:
#     print("Добро пожаловать!")
# else: 
#     print("Неверный логин или пароль")


crit1 = "red"
crit2 = "lock"

colour = input("Colour: ")
feature = input("Feature: ")

if (colour == crit1) or (feature == crit2):
    print("Покупаю рюкзак")
else:
    print("Ничего не подошло")