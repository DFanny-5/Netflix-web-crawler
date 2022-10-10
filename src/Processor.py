from utils import time_transfer, date_transfer, pattern_search
from ErrorHandler import ErrorHandler

class Processor:
    def __init__(self, page_soup, entry_record):
        self.page_soup = page_soup
        self.record = entry_record

    def proces_and_record(self):
        self.record.title = self.generate_title()
        self.record.genre = self.generate_genre()
        self.record.cast = self.generate_cast()
        self.record.director = self.generate_director()
        self.record.time_duration = self.generate_duration()
        self.record.added_date, self.record.added_month, self.record.added_year = self.generate_available_date()
        self.record.parent_control = self.generate_parent_control()
        self.record.original_language = self.generate_original_language()
        self.record.subtitle = self.generate_subtitle()
        self.record.description = self.generate_description()
        return self.record

    @ErrorHandler.handle_scrap_error
    def generate_title(self):
        return self.page_soup.find('a', title=True).getText()

    @ErrorHandler.handle_scrap_error
    def generate_genre(self):
        for genre_field in self.page_soup.find_all('div', "genre"):
            if genre := genre_field.find('h5'):
                return genre.getText()

    @ErrorHandler.handle_scrap_error
    def generate_cast(self):
        cast_field = self.page_soup.find("strong", string="Cast:").parent  # <class 'bs4.element.Tag'>
        return [cast.getText() for cast in cast_field.find_all("a")]

    @ErrorHandler.handle_scrap_error
    def generate_director(self):
        director_field = self.page_soup.find("strong", string="Director:").parent
        return [director.getText() for director in director_field.find_all("a")]

    @ErrorHandler.handle_scrap_error
    def generate_duration(self):
        return time_transfer(self.page_soup.find("strong", string="Duration:").nextSibling)

    @ErrorHandler.handle_scrap_error
    def generate_available_date(self):
        return date_transfer(self.page_soup.find("strong", string="Date Added:").nextSibling)

    @ErrorHandler.handle_scrap_error
    def generate_parent_control(self):
        return self.page_soup.find("span", "ratingsblock").getText()

    @ErrorHandler.handle_scrap_error
    def generate_original_language(self):
        languages = self.page_soup.find("strong", string="Audio:").nextSibling
        original_pattern = r'(\w*)(?=[ ]*\[Original\])'
        original_language = pattern_search(original_pattern, languages).group(1)
        return original_language

    @ErrorHandler.handle_scrap_error
    def generate_subtitle(self):
        subtitles = self.page_soup.find("strong", string="Subtitles:").nextSibling
        return [subtitle.strip() for subtitle in subtitles.split(',')]

    @ErrorHandler.handle_scrap_error
    def generate_description(self):
        return self.page_soup.find("strong", string="Description:").parent.nextSibling.getText()