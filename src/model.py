class MovieEntry:

    def __init__(self, page_url, item_id):
        self.page_url = page_url
        self.id = item_id
        self.title = None
        self.genre = None
        self.cast = None
        self.director = None
        self.time_duration = None
        self.added_date = None
        self.added_month = None
        self.added_year = None
        self.parent_control = None
        self.original_language = None
        self.subtitle = None
        self.description = None

    def __str__(self):
        return str(vars(self))

    def get_title(self):
        return self.title
