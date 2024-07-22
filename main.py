import os
import sys
from src.get_vacancies import HHruAPI, CreateJson
from src.utils import sort_by_salary, sort_by_date, get_exchange_rate, without_sort, change_currency
from src.file_worker import JsonWorker
from src.user_interface import create_request_phrase, made_json, option_sort


def user_interaction():
    print('Привет! С помощью этой программы ты можешь найти работу.')
    vacancies = create_request_phrase()
    print(f'В случае указания зарплаты в USD, зарплата будет конвертирована в RUB по курсу: {get_exchange_rate()}')
    made_json(vacancies)
    print(f'Найдено {len(vacancies)} вакансий:')
    # path_to_file = os.path.abspath('data/vacancies.json')
    js = JsonWorker()  # создаем объект класса JsonWorker
    opend_json = js.open_file() # открываем файл json
    change_currency_to_rub = change_currency(opend_json) # конвертируем зарплату в рубли из USD
    option_sort(change_currency_to_rub)

    print('\nКонец программы, все вакансии были выведены на экран')


if __name__ == "__main__":
    user_interaction()