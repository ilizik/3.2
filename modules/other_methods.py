import re


class OtherMethods:
    """Класс, содержащий в себе вспомогатильные функции которые могут быть переиспользованы"""

    @staticmethod
    def delete_rubbish(s: str) -> str:
        """Удаляет html теги и лишние пробелы из строки
        :param s: Строка для чистки
        :return: Очищенная строка
        """
        clear = re.compile('<.*?>')

        return ' '.join(re.sub(clear, '', s).split()).strip()

    @staticmethod
    def normalize_label(label: str) -> str:
        """Форматирует подписи круговой даиграммы
        :param label: Подпись
        :return: Отформатированная подпись
        """
        spaces = re.compile('\s+')
        line = re.compile('-+')

        label = re.sub(spaces, '\n', label)
        return re.sub(line, '-\n', label)