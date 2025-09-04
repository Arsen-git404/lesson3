from smartphone import Smartphone


catalog = [
    Smartphone(mark_phone="Samsung", model="Galaxy Z Fold6",
               phone_number="+79144591234"),
    Smartphone(mark_phone="Apple", model="IPhone 17 Pro Max",
               phone_number="+79234567890"),
    Smartphone(mark_phone="Xiaomi", model="14T Pro",
               phone_number="+79123402895"),
    Smartphone(mark_phone="Nokia", model="3310",
               phone_number="+79231354790"),
    Smartphone(mark_phone="Apple", model="Black Diamond iPhone 5",
               phone_number="+79638422552")
]


for smartphone in catalog:
    print(f"{smartphone.mark} - {smartphone.model}. {smartphone.number}")