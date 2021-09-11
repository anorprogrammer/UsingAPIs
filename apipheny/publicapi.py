import requests
from pprint import pprint




# Entries-Yozuvlar
# API Bosh sahifasi
# URL: https://api.publicapis.org/entries
URL = "https://api.publicapis.org/entries"
response = requests.get(url=URL)
response_json = response.json()

# To'liq json ni chiqarish !
pprint(response_json)

# Faqat API larning o'zini chiqarish
# pprint(response_json['entries'])

# n-API ni chiqarish
# pprint(response_json['entries'][0])

# API ma'lumotlarini olish
# pprint(response_json['entries'][0]['API'])
# pprint(response_json['entries'][0]['Description'])
# pprint(response_json['entries'][0]['HTTPS'])
# pprint(response_json['entries'][0]['Link'])

# Turli kategoriyalar bo'yicha qidirish
# URL: https://api.publicapis.org/entries/entries?category=animals&https=true
# category = "animals"
# protocol = "true"
# URL2 = f"https://api.publicapis.org/entries?category={category}&https={protocol}"
# URL3 = f"https://api.publicapis.org/entries?auth=OAuth"
# response = requests.get(url=URL3)
# response_json = response.json()
# pprint(response_json)


# Tasodifiy API ni olish
# URL4 = "https://api.publicapis.org/random"
# response = requests.get(url=URL4)
# response_json = response.json()
# pprint(response_json)

# Tasodifiy API ni categoriyalar bo'yich olish
# URL5 = "https://api.publicapis.org/random?auth=null"
# response = requests.get(url=URL5)
# response_json = response.json()
# pprint(response_json)