from urllib.request import Request, urlopen
import json
import sys
from datetime import *
import xmltodict


def json_request(url = '', encoding = 'utf-8', success = None,
                 error = lambda e : print('%s %s' % (e, datetime.now()), file=sys.stderr)):
    try:
        request = Request(url)
        resp = urlopen(request)
        json_body = resp.read().decode(encoding)

        xml_dict = xmltodict.parse(json_body)       # xml형식을 dict로 파싱
        dict_json = json.dumps(xml_dict)
        json_result = json.loads(dict_json)

        print('%s : success for request [%s]' % (datetime.now(), url))



        if callable(success) is False:
            return json_result

        success(json_result)
    except Exception as e:
        if callable(error) is True:
            error(e)