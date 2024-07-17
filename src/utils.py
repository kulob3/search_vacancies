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
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data['Valute']['USD']['Value']
    except requests.RequestException as e:
        print(f"Ошибка при получении курса валюты: {e}. Курс валюты установлен по умолчанию: ")
        return 90.0

def change_currency(path_to_file):
    """
        Открывает json и конвертирует зарплату в вакансиях из USD в RUB
    """
    path_vacancies = os.path.abspath(path_to_file)
    with open(path_vacancies, 'r', encoding='utf-8') as file:
        list_vacancies = js.loads(file.read())
        for i in list_vacancies:
            if i['currency'] == 'USD':
                i['salary'] = i['salary'] * get_exchange_rate() if i['salary'] else None
                i['currency'] = 'RUB (конвертировано из USD)'
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

