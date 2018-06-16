from collect.api import api
import json


url = api.bus_gen_url(busRouteId=100100112, _type='json')
print(url)

item = api.bus_fetch_info(busRouteId=100100112)
print(item)