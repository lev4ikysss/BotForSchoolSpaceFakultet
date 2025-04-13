def raise_error(error_msg):
    raise ApiError(f'{error_msg}')


class ApiError(Exception):
    __slots__ = 'text'

    def __init__(self, text):
        self.text = text
