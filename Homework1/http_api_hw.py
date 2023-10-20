import requests
import time

# Send request to thinkspeak
def thinkspeak_get_url_encoded():
    url = 'https://api.thingspeak.com/update?api_key=UZJ7D5KZB4T1DU4X&field1=20&field2=33'
    response = requests.get(url)
    print(response.json())

def thinkspeak_get_json():
    # Use body request
    body_request = {
        'api_key': 'UZJ7D5KZB4T1DU4X',
        'field1': 50,
        'field2': 43
    }

    # Send request to thinkspeak
    url = 'https://api.thingspeak.com/update'
    response = requests.get(url, json=body_request)
    print(response.json())


def thinkspeak_get_data():
    url = 'https://api.thingspeak.com/channels/2302713/feeds.json?api_key=DRLH1MYHE1H3IULD&results=2'
    response = requests.get(url)
    # parse json to get data of field1 and field2
    data = response.json()
    print('-' * 5)
    print('Data of field1:')
    print(data['feeds'][-1]['field1'])
    print('-' * 5)
    print('Data of field2:')
    print(data['feeds'][-1]['field2'])

if __name__ == '__main__':
    print('Gửi dữ liệu gồm 2 trường field1, field2 lên Thinkspeak qua API theo 2 cách')
    print('-' * 5)
    print('Cách 1:')
    thinkspeak_get_url_encoded()
    print('-' * 5)
    time.sleep(20)
    print('Cách 2:')
    thinkspeak_get_json()
    print('-' * 20)
    print('Lấy dữ liệu về từ Thingspeak API')
    print('-' * 5)
    thinkspeak_get_data()
