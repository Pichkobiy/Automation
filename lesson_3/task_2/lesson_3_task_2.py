from smartphone import Smartphone

catalog = []

phone_1 = Smartphone('nokia', 'XR20', '+78965602413')
phone_2 = Smartphone('xiaomi', 'Realme C51', '+79536221475')
phone_3 = Smartphone('motorolla', 'G45', '+79635478596')
phone_4 = Smartphone('xiaomi', '13T Pro', '+78539656398')
phone_5 = Smartphone('samsung', 'S24 Ultra', '+79568745242')

catalog.append(phone_1)
catalog.append(phone_2)
catalog.append(phone_3)
catalog.append(phone_4)
catalog.append(phone_5)

for phone in catalog:
    print(f"{phone.brand}{phone.model}-{phone.phone_number}")