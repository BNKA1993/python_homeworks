from adress import Address
from Mailing import Mailing

to_adress = Address("656000", "Moskow", "Lenina", "20", "456")
from_adress = Address("656456", "Spb", "Pushkina", "40", "1")

mailing = Mailing(to_adress, from_adress, 560, "track12345")

print(f"Отправление {mailing.track} из {mailing.from_adress.index}, {mailing.from_adress.city}, {mailing.from_adress.street}, {mailing.from_adress.house}, {mailing.from_adress.flat} в {mailing.to_adress.index}, {mailing.to_adress.city}, {mailing.to_adress.street}, {mailing.to_adress.house}, {mailing.to_adress.flat}. Стоимость {mailing.cost} рублей")