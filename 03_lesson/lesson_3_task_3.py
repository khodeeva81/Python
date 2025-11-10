
from address import Address
from mailing import Mailing


to_addr = Address(
    index='123456',
    city='Москва',
    street='Ленина',
    house='10',
    apartment='15'
)


from_addr = Address(
    index='654321',
    city='Санкт-Петербург',
    street='Невский',
    house='5',
    apartment='22'
)


mail = Mailing(
    to_address=to_addr,
    from_address=from_addr,
    cost=500,
    track='ABC123456789'
)


print(
    f"Отправление {mail.track} из {mail.from_address.index}, {mail.from_address.city}, "
    f"{mail.from_address.street}, {mail.from_address.house} - {mail.from_address.apartment} "
    f"в {mail.to_address.index}, {mail.to_address.city}, {mail.to_address.street}, "
    f"{mail.to_address.house} - {mail.to_address.apartment}. "
    f"Стоимость {mail.cost} рублей."
)
