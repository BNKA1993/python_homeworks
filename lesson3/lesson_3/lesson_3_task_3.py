from adress import Address
from Mailing import Mailing

to_adress = Address("656000", "Moskow", "Lenina", "20", "456")
from_adress = Address("656456", "Spb", "Pushkina", "40", "1")

mailing = Mailing(to_adress, from_adress, 560, "track12345")

print(f"Отправление {mailing.track} из {mailing.from_adress.show_adress()} в {mailing.to_adress.show_adress()}. Стоимость {mailing.cost} рублей")
