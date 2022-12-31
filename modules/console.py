class Console:
    """Класс, представляющий взаимодействие с консолью
    Attributes:
        file_name (str): Название файла
    """
    def __init__(self):
        """Инициализирует объект класcа"""
        self.file_name: str = ''

    def read_console(self):
        """Читает данные с консоли"""
        self.file_name = input('Введите название файла: ')
