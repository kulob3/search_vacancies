import requests
import json as js
import os
from src.vacancies import Vacancies

def get_exchange_rate():
    """
    Получает текущий курс обмена рубля к доллару США.
    Использует API Центрального Банка России.
    """
    url = "https://www.cbr-xml-daily.ru/daily_json.js"
    try:
        response = requests.get(url, timeout=10)  # Установка времени ожидания запроса 10 секунд
        response.raise_for_status()
        data = response.json()
        return data['Valute']['USD']['Value']
    except requests.RequestException as e:
        print(f"Ошибка при получении курса валюты: {e}. Курс валюты установлен по умолчанию: ")
        return 90.0

def change_currency(opened_json):
    """
        Конвертирует зарплату в вакансиях из USD в RUB
    """
    # path_vacancies = os.path.abspath(path_to_file)
    # with open(path_vacancies, 'r', encoding='utf-8') as file:
    list_vacancies = []
    for i in opened_json:
        if i['currency'] == 'USD':
            i['salary'] = i['salary'] * get_exchange_rate() if i['salary'] else None
            i['currency'] = 'RUB (конвертировано из USD)'
        list_vacancies.append(i)
    return list_vacancies

def without_sort(list_vacancies):
    """
    Сортирует список вакансий по порядку
    """
    sorted_vacancies = []
    for i in list_vacancies:
        sorted_vacancies.append(
            Vacancies(i['name'], i['employer'], i['salary'], i['currency'], i['experience'],
                      i['employment'], i['area'], i['published_at'], i['alternate_url']))
    return sorted_vacancies

def sort_by_salary(list_vacancies):
    """
        Сортирует список вакансий по зарплате
    """
    vacancies_sort = sorted(list_vacancies, key=lambda x: int(x['salary']) if isinstance(x['salary'], int) else (int(x['salary']) if isinstance(x['salary'], str) and x['salary'].isdigit() else 0), reverse=True)
    sorted_vacancies = []
    for i in vacancies_sort:
        sorted_vacancies.append(
            Vacancies(i['name'], i['employer'], i['salary'], i['currency'], i['experience'],
                      i['employment'], i['area'], i['published_at'], i['alternate_url']))
    return sorted_vacancies

def sort_by_date(list_vacancies):
    """
        Сортирует список вакансий по дате размещения
    """
    vacancies_sort = sorted(list_vacancies, key=lambda x: x['published_at'], reverse=True)
    sorted_vacancies = []
    for i in vacancies_sort:
        sorted_vacancies.append(
            Vacancies(i['name'], i['employer'], i['salary'], i['currency'], i['experience'],
                      i['employment'], i['area'], i['published_at'], i['alternate_url']))
    return sorted_vacancies

def comparison_salary(salary_size, change_currency_to_rub):
    # Assuming 'salary_size' is an integer and 'change_currency_to_rub' is a list of dictionaries
    # with each dictionary representing a vacancy and containing a 'salary' key.
    v = Vacancies('Python developer', 'Company', salary_size, 'RUB', '1 year', 'full-time', 'Moscow', '2021-09-01T00:00:00+0300', 'https://hh.ru')
    salary_by_level = []
    for i in change_currency_to_rub:
        # Assuming 'salary' is the key in the dictionary 'i' that holds the salary value
        # and 'v.salary' accesses the salary attribute of the Vacancies object.
        # You need to replace 'v.salary' with the actual way to access the salary from a Vacancies object.
        if 'salary' in i and i['salary'] is not None and v.salary is not None and i['salary'] >= v.salary:  # Replace 'v.salary' with the correct attribute access
            salary_by_level.append(
            Vacancies(i['name'], i['employer'], i['salary'], i['currency'], i['experience'],
                      i['employment'], i['area'], i['published_at'], i['alternate_url']))
    return salary_by_level




