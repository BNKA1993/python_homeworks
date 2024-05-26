from smartphone import Smartphone

catalog = [
    Smartphone("Xiaomi", "12TPro", "+79998887766"),
    Smartphone("Apple", "15", "+79364382974"),
    Smartphone("Samsung", "Pro", "+79364888881"),
    Smartphone("Nokia", "Max", "+79322222222"),
    Smartphone("Siemence", "3", "+79343567897")
]

for phone in catalog:
    print(f'{phone.brend} - {phone.model} - {phone.phone_number}')