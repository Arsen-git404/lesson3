from mailing import Mailing
from address import Address


to_address = Address("675000", "Благовещенск", "Ленина", "135", "1")
from_addres = Address("103274", "Москва", "Краснопресненская набережная", "2" , "2")

Mail = Mailing(to_address, from_addres, 250, "TRK123456")

print(
f"Отправление {Mail.track} из {Mail.from_address.index},  {Mail.from_address.city}, {Mail.from_address.street}, {Mail.from_address.house} - {Mail.from_address.flat} "
f" в {Mail.to_address.index}, {Mail.to_address.city}, {Mail.to_address.street}, {Mail.to_address.house} - {Mail.to_address.flat}."
      f" Стоимость {Mail.cost} рублей "
)