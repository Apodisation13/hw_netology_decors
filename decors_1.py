from datetime import datetime
from os import path
import sys


sys.path.append('D:\\Python Projects')
print(sys.path)
from highl_try.wiki_try import input_json_reader


def log_writer_with_path(file_path):
    def write_logger(func):
        def logger(*args, **kwargs):
            start = datetime.now()
            print(f'Функция {func.__name__}')
            func_result = func(*args, **kwargs)
            end = datetime.now()
            time_result = end - start
            print(f'Время выполнение функции {func.__name__} - {time_result}')
            with open(file_path, 'a+', encoding='utf-8') as out:
                out.write(f'{start}, '
                          f'функция {func.__name__}, время выполнения {time_result},'
                          f'агрументы - {args}, {kwargs},'
                          f'вернёт - {func_result},'
                          f'путь логера - {path.abspath(file_path)}\n')
            print('log file updated')

        return logger

    return write_logger


@log_writer_with_path(file_path='output.txt')
def c():
    cc = [i for i in range(0, 40000000, 2)]
    # return cc  # НЕЕЕЕТ, вот так делать нельзя......)) иначе в выходной файл запишутся все числа 0,1,2,3,4 итп


@log_writer_with_path('output.txt')
def d(number, step):
    dd = (i for i in range(0, number, step))
    return dd


@log_writer_with_path('output.txt')
def json_reader_from_another_project():
    file = input_json_reader('countries.json')
    return len(file)


if __name__ == "__main__":
    c()
    d(40000000, step=2)
    json_reader_from_another_project()
