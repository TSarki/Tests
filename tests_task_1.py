import requests
import pytest
from unittest.case import TestCase
from main import visit_russia, max_stats_value, unique_id, stats, geo_logs, ids, my_token, YandexDisk

class TestMain(TestCase):
    def test_visit_russia(self):
        res = visit_russia(geo_logs)
        self.assertEqual(type(res), list)
        for log in res:
            for dict in log.values():
                self.assertIn('Россия', dict)
                
    def test_unique_id(self):
        res = unique_id(ids)
        self.assertEqual(type(res), set)
        list_1 = list(ids.values())
        list_2 = []
        for nums in list_1:
            for num in nums:
                list_2.append(num)
        self.assertEqual(set(list_2), res)
        
    def test_max_stats_value(self):
        res = max_stats_value(stats)
        self.assertEqual(res, 'Максиальное количество запросов у канала yandex')
        
    def test_yandex(self):
        yandex = YandexDisk(my_token)
        res = yandex.upload_file_to_disk('/photo.jpg', 'photo.jpg')
        self.assertTrue(res, 201)

    def setUp(self) -> None:
        self.token = my_token

    def test_file_exists(self):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/photo.jpg"
        headers = YandexDisk.get_headers(self)
        params = {"path": '/photo.jpg', "overwrite": "true"}
        res = requests.get(upload_url, headers=headers, params=params)
        self.assertTrue(res.status_code, 201)
        
    def tearDown(self) -> None:
        del self.token