import phonenumbers
from phonenumbers import geocoder, carrier,timezone 
x=int(input('Enter the phone number: '))
phoneNumber = phonenumbers.parse("+91%d"%x) 
Carrier =carrier.name_for_number(phoneNumber, 'en') 
Region = geocoder.description_for_number(phoneNumber, 'en')
timeZone = timezone.time_zones_for_number(phoneNumber)  
print(Carrier,'\n',Region,'\n',timeZone) 
