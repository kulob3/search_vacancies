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
        print(f"Ошибка при получении курса валюты: {e}")
        return None

# def open_json(path_to_file):
#     """
#         Получает список вакансий из vacancies.json
#     """
#     path_vacancies = os.path.abspath(path_to_file)
#     with open(path_vacancies, 'r', encoding='utf-8') as file:
#         list_vacancies = js.loads(file.read())
#         vacancies_sort = []
#         # return list_vacancies
#         for i in list_vacancies:
#             vacancies_sort.append(Vacancies(i['name'], i['employer'], i['salary']['from'], i['salary']['currency'], i['experience'], i['employment'], i['area'], i['published_at'], i['alternate_url']))
#         return vacancies_sort

def sort_by_salary(path_to_file):
    """
        Сортирует список вакансий по зарплате
    """
    path_vacancies = os.path.abspath(path_to_file)
    with open(path_vacancies, 'r', encoding='utf-8') as file:
        list_vacancies = js.loads(file.read())
        for i in list_vacancies:
            if i['salary']['currency'] == 'USD':
                i['salary']['from'] = i['salary']['from'] * get_exchange_rate() if i['salary']['from'] else None
                i['salary']['to'] = i['salary']['to'] * get_exchange_rate() if i['salary']['to'] else None
                i['salary']['currency'] = 'RUB'
        vacancies_sort = sorted(list_vacancies, key=lambda x: x['salary']['from'] if x['salary']['from'] else 0, reverse=True)
        sorted_vacancies = []
        print(f'\nНайдено {len(vacancies_sort)} вакансий:')
        for i in vacancies_sort:
            sorted_vacancies.append(
                Vacancies(i['name'], i['employer'], i['salary']['from'], i['salary']['currency'], i['experience'],
                          i['employment'], i['area'], i['published_at'], i['alternate_url']))
        return sorted_vacancies





if __name__ == "__main__":
    print(get_exchange_rate())
    obj = sort_by_salary('..//data/vacancies.json')
    for i in obj:
        print(i.__str__())




    # for i in open_json('..//data/vacancies.json'):
    #     print(i['name'])
    #     print(i['employer'])
    #     print(i['salary'])
    #     print(i['experience'])
    #     print(i['employment'])
    #     print(i['area'])
    #     print(i['published_at'])
    #     print(i['alternate_url'])