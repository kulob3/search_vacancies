from abc import ABC, abstractmethod
import requests
import os
import json

class VacancyServiceAPI(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def load_vacancies(self, query):
        pass

class HHruAPI(VacancyServiceAPI):
    base_url = "https://api.hh.ru/vacancies"

    def connect(self):
        # Проверка подключения к API
        try:
            response = requests.get(self.base_url)
            response.raise_for_status()
            print("\nConnection successful")
        except requests.exceptions.RequestException as e:
            print(f"\nConnection failed: {e}")

    def load_vacancies(self, query):
        # Загрузка вакансий
        params = {'text': query, 'page': 0, 'per_page': 100}
        vacancies = []
        while params.get('page') != 20:
            response = requests.get(self.base_url, params=params)
            vacancies.extend(response.json()['items'])
            params['page'] += 1
        return vacancies


class CreateJson:
    def __init__(self, filename):
        self.filename = filename

    def write(self, data):
        all_data = []
        for i in data:
            new_json = {
                'name': i['name'],
                'employer': i['employer']['name'],
                'salary': i['salary'],
                'experience': i['experience']['name'],
                'employment': i['employment']['name'],
                'area': i['area']['name'],
                'published_at': i['published_at'],
                'alternate_url': i['alternate_url']
            }
            all_data.append(new_json)

        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(all_data, file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    hh = HHruAPI()
    hh.connect()
    vacancies = hh.load_vacancies("Python Москва зарплата от 100000")

    cj = CreateJson('..//data/vacancies.json')
    cj.write(vacancies)

    for i in vacancies:
        print(i['name'])
        print(i['employer']['name'])
        print(i['salary'])
        print('experience:', i['experience']['name'])
        print('employment:', i['employment']['name'])
        print('area:', i['area']['name'])
        print(i['published_at'])
        print(i['alternate_url'])