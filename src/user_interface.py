import os
import sys
from src.get_vacancies import HHruAPI, CreateJson
from src.utils import sort_by_salary, sort_by_date, get_exchange_rate, without_sort, change_currency
from src.file_worker import JsonWorker

def create_request_phrase():
    search_query = input("Введите наименование специальности для запроса: ")
    search_salary = input("Введите минимальную зарплату для запроса, для поиска без учета размера зарплаты нажмите 'Enter': ")
    if not search_salary:
        search_salary = ''
    search_sity = input("Введите город для запроса, для поиска без учета города нажмите 'Enter': ")
    if not search_sity:
        search_sity = ''
    hh = HHruAPI()  # Создаем объект класса HHruAPI
    hh.connect()  # Устанавливаем соединение с HH.ru
    vacancies = hh.load_vacancies(f"{search_query} {search_sity} зарплата от {search_salary}")
    return vacancies

def made_json(vacancies):
    cj = CreateJson('data/vacancies.json')  # создаем объект класса CreateJson
    cj.write(vacancies)  # создаем json-файл для работы с вакансиями

import os

def get_file_path(filename):
    return os.path.abspath(filename)
print(get_file_path('data/vacancies.json'))
