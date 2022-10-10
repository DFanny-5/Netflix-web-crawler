import re
import itertools

import config
from model import MovieEntry
from Processor import Processor
from HttpClient import HttpClient
from utils import create_page_index
from MetaDataSerializer import MataDataSerializer


class NetflixCrawler:
    def __init__(self):
        self.total_processed_record = 0
        self.indexed_home_page = []

    def run(self, main_url):
        index_list = create_page_index()
        page_index_urls = [main_url + index for index in index_list]
        for index_page_url in page_index_urls:
            self.indexed_home_page.extend(self.indexed_url_generator(index_page_url))
        record_csv_path = MataDataSerializer.check_csv_file_existence(config.MOVIE_CSV_PATH, MovieEntry)
        data_serializer = MataDataSerializer(record_csv_path)
        last_number = int(MataDataSerializer.generate_value_last_exist_row(record_csv_path, 1))
        new_id = itertools.count(last_number)
        for index_page_url in self.indexed_home_page:
            for item_url_suffix in self._individual_url_generator(HttpClient(index_page_url).get_soup()):
                item_url = config.INDIVIDUAL_URL_PREFIX + item_url_suffix
                item_url_soup = HttpClient(item_url).get_soup()
                item_entry_record = MovieEntry(item_url, next(new_id))
                item_processor = Processor(item_url_soup, item_entry_record)
                entry_record = item_processor.proces_and_record()
                data_serializer.add_entry(entry_record)

    def indexed_url_generator(self, index_page):
        index_page_soup = HttpClient(index_page).get_soup()
        item_n_under_index = int(self._get_number_of_items(index_page_soup))
        print(f"find {item_n_under_index} items under {index_page}")
        split_page_urls = []
        for split_page in self._split_index_page(index_page, item_n_under_index):
            split_page_urls.append(split_page)
        return split_page_urls

    @staticmethod
    def _get_number_of_items(soup_instance):
        search_key_word_titles = soup_instance.find_all(string=re.compile(r"\d+ titles"))[0]
        title_number_pattern = r'(\d+) titles'
        return re.search(title_number_pattern, str(search_key_word_titles)).group(1)

    @staticmethod
    def _split_index_page(url_suffix: str, total_items_numbers: int):
        sub_page_number = total_items_numbers // config.ITEM_PER_PAGE + 1
        print('{0} has {1} movies/tv show,split into {2} separate index pages'.format(url_suffix,total_items_numbers,
                                                                          sub_page_number))
        for i in range(sub_page_number):
            yield f'{url_suffix}/?start={i * 120}#results'

    def _individual_url_generator(self, index_page_soup):
        search_results = index_page_soup.find_all('a', {'class': 'infopop'}, href=re.compile('/info'), title=True)
        for search_result in search_results:
            yield search_result.attrs['href']





if __name__ == '__main__':
    movie_url = 'https://can.newonnetflix.info/catalogue/a2z/movies'
    NetflixCrawler().run(movie_url)
    #record_csv_path = MataDataSerializer.check_csv_file_existence(config.MOVIE_CSV_PATH, MovieEntry)
    #print(record_csv_path)
    pass
