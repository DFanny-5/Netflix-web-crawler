import requests
from bs4 import BeautifulSoup


class HttpClient:
    def __init__(self, url):
        r = self.request_with_header(url)
        self.url = url
        self.soup = BeautifulSoup(r.text, 'html.parser')

    @staticmethod
    def request_with_header(url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ''Chrome/51.0.2704.63 Safari/537.36'}
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        return response

    def get_url(self):
        return self.url

    def get_soup(self):
        return self.soup
