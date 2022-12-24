import requests

geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

my_token = 'y0_AgAAAAA2DWi0AADLWwAAAADSbv5sysfF9A6MSj-r_BaPm0jCYjTXFjQ'

stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

def visit_russia(geo_logs):
    for dict_ in reversed(geo_logs):
        for countries in dict_.values():
            if 'Россия' not in countries:
                geo_logs.remove(dict_)
    return geo_logs  


def unique_id(ids):
    ids_new = list(ids.values())
    sort_set = set(ids['user1'])
    for items in ids_new:
        for integers in items:
            sort_set.add(integers)
    return sort_set


def max_stats_value(stats):
    for keys, values in stats.items():
        if values == max(stats.values()):
            return f'Максиальное количество запросов у канала {keys}'
        

class YandexDisk:

    def __init__(self, token):
        self.token = my_token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def upload_file_to_disk(self, disk_file_path, filename):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        href = response.json().get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        return response.status_code == 201
             



if __name__ == '__main__':
    visit_russia(geo_logs)
    unique_id(ids)
    max_stats_value(stats)
    yandex = YandexDisk(my_token)
    yandex.upload_file_to_disk('/photo.jpg', 'photo.jpg')