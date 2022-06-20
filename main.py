import requests

TOKEN = "AQAAAAAUGoLOAADLWxBpwOpsakazlD5giIGCs-M"
file_name = "HW8.txt"

class YandexDisk():
    def __init__(self, token):
        self.token = token

    def _get_path_to_ya_disk(self, disk_path):
        url = "https://cloud-api.yandex.net:443/v1/disk/resources/upload"
        headers = {"Content-Type": "application/json",
           "Authorization": f"OAuth {self.token}"}
        params = {"path": disk_path, "overwrite": "true"}
        response = requests.get(url=url, headers = headers, params = params)
        return response.json()

    def upload_file_to_ya_disk(self, disk_path, file_name):
        href = self._get_path_to_ya_disk(disk_path = disk_path).get("href", "")
        response = requests.put(href)
        response.raise_for_status()
        if response.status_code == 201:
             print("Success")

if __name__ == '__main__':
    ya = YandexDisk(token=TOKEN)
    # ya._get_path_to_ya_disk("HomeWork/myfile.txt")
    ya.upload_file_to_ya_disk("HomeWork/myfile.txt", "HW8.txt")

