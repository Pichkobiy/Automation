from address import Address
from mailing import Mailing

to_address = Address('185026', 'город Петрозаводск', 'улица Ровио', '13', '1')
from_address = Address('186870', 'город Суоярви', 'улица Садовая', '5', '37')
mailing = Mailing(to_address, from_address, '414', 'CA46678')

print(f'Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, '
      f'{mailing.from_address.street}, дом {mailing.from_address.house}, квартира {mailing.from_address.apartment}'
      f'в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, '
      f'дом {mailing.to_address.house}, квартира {mailing.to_address.apartment}.'
      f'Стоимость {mailing.cost} рублей.')