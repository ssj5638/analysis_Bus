from collect.api.json_requests import json_request
from urllib.parse import urlencode


BASE_URL_BUS_API = 'http://ws.bus.go.kr/api/rest/busRouteInfo/getRouteInfo'
SERVICE_KEY = 'EdieVeGWBCgcq7f02Z4gpx%2FEssqE8l151SGr%2FHYps1SvWYKgXvpn35kSxTQUhMkxyf9yOrp2SU%2Fr9xZjf7aWQA%3D%3D'


def bus_gen_url(base=BASE_URL_BUS_API, **params):
    url = '%s?ServiceKey=%s&%s' % (base, SERVICE_KEY, urlencode(params))
    return url


def bus_fetch_info(busRouteId=''):

    url = bus_gen_url(busRouteId=busRouteId)
    json_result = json_request(url = url)

    json_msgbody = json_result.get('ServiceResult').get('msgBody')

    return json_msgbody