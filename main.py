import phonenumbers
import opencage
import folium

number = "+33 6 61 98 64 99"

from phonenumbers import geocoder

ch_nmber = phonenumbers.parse(number)
location = geocoder.description_for_number(ch_nmber, "en")
print("hello")

from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "en"))

from opencage.geocoder import OpenCageGeocode

key = 'e5b581504c394327886679f1612d71eb'

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng)

myMap = folium.Map(location = [lat,lng] , zoom_start= 9)
folium.Marker([lat, lng], popup = location).add_to(myMap)
myMap.save("mylocation.html")