from .api import api
import json
import os


RESULT_DIRECTORY = '__results__/crawlling'


def preprocess_bus_info(data):
    if 'lastBusYn' in data:
        del data['lastBusYn']
    if 'lastLowTm' in data:
        del data['lastLowTm']
    if 'firstLowTm' in data:
        del data['firstLowTm']
    if 'firstLowTm' in data:
        del data['length']
    if 'busRouteId' not in data:
        data['busRouteId'] = 0
    else:
        data['노선 ID'] = data['busRouteId']
        del data['busRouteId']
    if 'busRouteNm' not in data:
        data['busRouteNm'] = 0
    else:
        data['노선 명'] = data['busRouteNm']
        del data['busRouteNm']
    if 'routeType' not in data:
        data['routeType'] = 0
    else:
        data['노선 유형'] = data['routeType']
        del data['routeType']
    if 'term' not in data:
        data['term'] = 0
    else:
        data['배차간격'] = data['term']
        del data['term']
    if 'stStationNm' not in data:
        data['stStationNm'] = 0
    else:
        data['기점'] = data['stStationNm']
        del data['stStationNm']
    if 'edStationNm' not in data:
        data['edStationNm'] = 0
    else:
        data['종점'] = data['edStationNm']
        del data['edStationNm']
    if 'firstBusTm' not in data:
        data['firstBusTm'] = 0
    else:
        data['금일첫차시간'] = data['firstBusTm']
        del data['firstBusTm']
    if 'lastBusTm' not in data:
        data['lastBusTm'] = 0
    else:
        data['금일막차시간'] = data['lastBusTm']
        del data['lastBusTm']
    if 'corpNm' not in data:
        data['corpNm'] = 0
    else:
        data['운수사명'] = data['corpNm']
        del data['corpNm']


def crawlling_bus_info(busRouteId):
    results=[]
    filename = '%s/bus_info_%s.json' % (RESULT_DIRECTORY, busRouteId)

    data = api.bus_fetch_info(busRouteId)

    preprocess_bus_info(data)
    results.append(data)

    with open(filename, 'w', encoding='utf-8') as outfile:
        json_string=json.dumps(results, indent=4, sort_keys=False, ensure_ascii=False)
        outfile.write(json_string)


if not os.path.exists(RESULT_DIRECTORY):
    os.makedirs(RESULT_DIRECTORY)