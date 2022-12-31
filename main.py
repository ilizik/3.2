from modules.csv_parser import CsvParser
from modules.console import Console


def main():
    """Функция для запуска программы
    :return:
    """
    connect = Console()
    connect.read_console()

    parser = CsvParser()
    parser.create_years_csv(connect.file_name, connect.output_dir)


if __name__ == '__main__':
    main()
