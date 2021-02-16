import os
import requests


def get_coordinates():
    base_url = 'http://api.ipstack.com/'
    api_key = os.environ.get("API_KEY")
    user_ip = '89.67.155.184'  # TODO take IP from API's user.

    request_url = base_url + 'check?access_key=' + api_key
    r = requests.get(request_url)
    data_json = r.json()
    json_dictionary = {'ip': data_json['ip'],
                       'latitude': data_json['latitude'],
                       'longitude': data_json['longitude']}

    # print('ip           = ', data_json['ip'])
    # print('latitude     = ', data_json['latitude'])
    # print('longitude    = ', data_json['longitude'])
    # print('\n', type(data_json))
    # print(request_url)
    print(json_dictionary)
    return json_dictionary


if __name__ == '__main__':
    get_coordinates()

# cd ~/Desktop/virenv/geolocation_api; . bin/activate; cd ~/Desktop/Programming/geolocation_api/geolocation;
# export API_KEY='5d4d1b71da56d93e933be4c4d6297153'
