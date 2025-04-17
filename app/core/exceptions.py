class SqlExeptions(Exception):
    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        return f'Ошибка SqlExeptions: {self.message}'