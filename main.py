import phonenumbers
from phonenumbers import timezone,geocoder,carrier
number=input("enter the phone number with you + and country code")
phone=phonenumbers.parse(number)
time=timezone.time_zones_for_number(phone)
car=carrier.name_for_number(phone,"en")
reg=geocoder.description_for_number(phone,"en")
print(phone)
print("network :",car)
print("cuntry :",reg)
print("time zone :",time)




