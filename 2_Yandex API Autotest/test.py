import requests
import unittest

class TestYandexDisk(unittest.TestCase):
    def setUp(self):
        self.base_url = "https://cloud-api.yandex.net/v1/disk/resources"
        with open('token.txt', 'r') as file:
            token = file.read().replace('\n', '')
        self.headers = {"Authorization": f"OAuth {token}"}

    def test_folder_creation(self):
        folder_path = "/test_folder"
        response = requests.put(self.base_url, headers=self.headers, params={"path": folder_path})
        self.assertEqual(response.status_code, 201)

    def test_folder_exists(self):
        folder_path = "/test_folder"
        response = requests.get(self.base_url, headers=self.headers, params={"path": folder_path})
        self.assertEqual(response.status_code, 200)

    def test_negative_case(self):
        wrong_folder_path = "/wrong_folder"
        response = requests.get(self.base_url, headers=self.headers, params={"path": wrong_folder_path})
        self.assertEqual(response.status_code, 404)

if __name__ == "__main__":
    unittest.main()