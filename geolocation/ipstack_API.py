import os
import requests
# import json


def get_coordinates():
    base_url = 'http://api.ipstack.com/'
    api_key = os.environ.get("API_KEY")
    filter_fields = '&fields=ip,latitude,longitude'

    request_url = base_url + 'check?access_key=' + api_key + filter_fields
    r = requests.get(request_url)
    data_json = r.json()
    # coordinate_dictionary = {'ip': data_json['ip'],
    #                          'latitude': data_json['latitude'],
    #                          'longitude': data_json['longitude']}
    # coordinate_json = json.dumps(coordinate_dictionary, indent=4)
    # return coordinate_dictionary
    return data_json


if __name__ == '__main__':
    print(get_coordinates())
