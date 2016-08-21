import json
import logging
import urllib
from copy import deepcopy

import urllib3
from django.http import JsonResponse
from django.shortcuts import render_to_response
from django.views import View

from api.tests import api_key

logger = logging.getLogger(__name__)


class Login(View):
    def get(self, request):
        # print(3333, request.GET['id'])
        g_api = GoogleMapApi(api_key)
        r = g_api.search_place("大阪城")
        r = json.loads(r)
        place_id = r['results'][0]['place_id']

        res = g_api.place_detail(place_id)
        res = json.loads(res)

        return render_to_response('login/login.html', locals())

    def post(self, request):
        return JsonResponse({'id': 'hello', 'vf': 123})


class GoogleMapApi:
    def __init__(self, api_key=None, resp_format='json'):
        self.__search_place_url = "https://maps.googleapis.com/maps/api/place/textsearch"
        self.__place_detail_url = "https://maps.googleapis.com/maps/api/place/details"

        self.__response_format = resp_format
        self.__api_key = api_key

        self.__API_PARAMS = {'key': self.__api_key}

        self.__http = urllib3.PoolManager()
        urllib3.disable_warnings()

    def search_place(self, place_name=""):
        params = self._get_default_params()
        params['query'] = place_name

        status, data = self._get_request(self.__search_place_url, params)

        return data

    def place_detail(self, place_id=""):
        params = self._get_default_params()
        params['placeid'] = place_id

        status, data = self._get_request(self.__place_detail_url, params)

        return data

    def _get_request(self, api_url, params):
        url = self._encode_url(api_url, params)
        resp = self.__http.request('GET', url)
        return resp.status, resp.data.decode('utf-8')

    def _encode_url(self, url, parameters):
        return url + '/' + self.__response_format + '?' + urllib.parse.urlencode(parameters)

    def _get_default_params(self):
        return deepcopy(self.__API_PARAMS)


def test(request):
    print(request.GET.get('id'))
    return render_to_response('login/login.html', locals())
