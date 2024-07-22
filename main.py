import os
import sys
from src.get_vacancies import HHruAPI, CreateJson
from src.utils import sort_by_salary, sort_by_date, get_exchange_rate, without_sort, change_currency
from src.file_worker import JsonWorker
from src.user_interface import create_request_phrase, made_json


def user_interaction():
    print('Привет! С помощью этой программы ты можешь найти работу.')
    vacancies = create_request_phrase()
    print(f'В случае указания зарплаты в USD, зарплата будет конвертирована в RUB по курсу: {get_exchange_rate()}')
    made_json(vacancies)
    print(f'Найдено {len(vacancies)} вакансий:')
    path_to_file = os.path.abspath('data/vacancies.json')
    js = JsonWorker(path_to_file)  # создаем объект класса JsonWorker
    opend_json = js.open_file() # открываем файл json
    change_currency_to_rub = change_currency(opend_json) # конвертируем зарплату в рубли из USD
    value_for_sort = input("Введите '1' для сортировки по зарплате, '2' для сортировки по дате размещения, 'Enter' - без сортировки: ")
    if value_for_sort == '1':
        vacancies_for_output = sort_by_salary(change_currency_to_rub)
    elif value_for_sort == '2':
        vacancies_for_output = sort_by_date(change_currency_to_rub)
    else:
        vacancies_for_output = without_sort(change_currency_to_rub)
    if len(vacancies_for_output) <= 20:
        for i in vacancies_for_output:
            print(i.__str__())
    else:
        batch_size = 20
        for start in range(0, len(vacancies_for_output), batch_size):
            end = start + batch_size
            for vacancy in vacancies_for_output[start:end]:
                print(vacancy.__str__())
            user_input = input("\nВведите 1, чтобы увидеть следующие вакансии или 2 для завершения работы программы: ")
            if user_input != '1':
                print('\nКонец программы')
                sys.exit()
    print('\nКонец программы, все вакансии были выведены на экран')


if __name__ == "__main__":
    user_interaction()