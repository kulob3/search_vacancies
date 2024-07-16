import os
from src.get_vacancies import HHruAPI, CreateJson
from src.vacancies import Vacancies
from src.utils import sort_by_salary, sort_by_date, get_exchange_rate,  change_currency, without_sort



def user_interaction():
    search_query = input("Введите наименование специальности для запроса: ")
    search_salary = input("Введите минимальную зарплату для запроса, для поиска без учета размера зарплаты нажмите 'Enter': ")
    if not search_salary:
        search_salary = ''
    search_sity = input("Введите город для запроса, для поиска без учета города нажмите 'Enter': ")
    if not search_sity:
        search_sity = ''
    hh = HHruAPI()
    hh.connect()
    print(f'В случае указания зарплаты в USD, зарплата будет конвертирована в RUB по курсу: {get_exchange_rate()}')
    vacancies = hh.load_vacancies(f"{search_query} {search_sity} зарплата от {search_salary}")
    cj = CreateJson('data/vacancies.json')
    cj.write(vacancies)
    print(f'Найдено {len(vacancies)} вакансий:')
    path_to_file = os.path.abspath('data/vacancies.json')
    change_currency_to_rub = change_currency(path_to_file)
    value_for_sort = input("Введите '1' для сортировки по зарплате, '2' для сортировки по дате размещения, 'Enter' - без сортировки: ")
    if value_for_sort == '1':
        vacancies_for_output = sort_by_salary(change_currency_to_rub)
    elif value_for_sort == '2':
        vacancies_for_output = sort_by_date(change_currency_to_rub)
    else:
        vacancies_for_output = without_sort(change_currency_to_rub)

    # vacancies_per_salary = sort_by_salary(path_to_file)
    # vacancies_per_date = sort_by_date(change_currency_to_rub)
    for i in vacancies_for_output:
        print(i.__str__())

if __name__ == "__main__":
    user_interaction()