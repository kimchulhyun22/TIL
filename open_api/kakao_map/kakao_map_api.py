# coding=utf-8
import requests
import config
import traceback
import datetime


class KakaoMapAPI:
    def __init__(self, api_key):
        self.headers = {
            'Authorization': 'KakaoAK ' + api_key
        }

        self.keyword_search_url = 'https://dapi.kakao.com/v2/local/search/keyword.json'

    def search_keyword_within_radius(self, keyword: str, page_num: int,
                                     latitude: float, longitude: float, radius: int):
        try:

            params = {
                'query': keyword,
                'page': page_num,
                'x': latitude,
                'y': longitude,
                'radius': radius,
            }

            response = requests.get(self.keyword_search_url, params=params, headers=self.headers).json()

            places = response['documents']

            return places

        except:
            print(traceback.format_exc())

        return None

    def search_category_within_radius(self):
        pass


start = datetime.datetime.now()

count = 1

kakao_map_api = KakaoMapAPI(config.KAKAO_APP_KEY)

while True:

    search_list = kakao_map_api.search_keyword_within_radius(keyword='스크린 골프', page_num=count, latitude=127.1086,
                                                             longitude=37.4021, radius=1000)

    if not search_list:
        break

    count += 1

    for search in search_list:
        print(search)

end = datetime.datetime.now()

print('총 크롤링 갯수 = {} 걸린시간 : {}'.format(count, (end - start).seconds))
