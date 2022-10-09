class ErrorHandler:

    @staticmethod
    def handle_scrap_error(f):
        def wrapper(*args, **kw):
            try:
                return f(*args, **kw)
            except Exception:
                print('I am triggered')
                return None

        return wrapper