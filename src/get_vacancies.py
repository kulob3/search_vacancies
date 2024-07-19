from abc import ABC, abstractmethod
import requests
import json

class VacancyServiceAPI(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def load_vacancies(self, query):
        pass

class HHruAPI(VacancyServiceAPI):
    ''' Класс для загрузки вакансий с HH.ru '''

    __base_url = "https://api.hh.ru/vacancies"

    def connect(self):
        # Проверка подключения к API
        try:
            response = requests.get(self.base_url)
            response.raise_for_status()
            print("Соединение с HH.ru установлено")
        except requests.exceptions.RequestException as e:
            print(f"Ошибка соединения: {e}")

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
    ''' Класс для создания файла json из списка'''
    def __init__(self, filename):
        self.__filename = filename

    @property
    def filename(self):
        return self.__filename

    @filename.setter
    def filename(self, value):
        self.__filename = value

    def write(self, data):
        all_data = []
        for i in data:
            new_json = {
                'name': i['name'],
                'employer': i['employer']['name'],
                'salary': i['salary']['from'] if i['salary'] else 'Не указана',
                'currency': i['salary']['currency'] if i['salary'] else '',
                'experience': i['experience']['name'],
                'employment': i['employment']['name'],
                'area': i['area']['name'],
                'published_at': i['published_at'],
                'alternate_url': i['alternate_url']
            }
            all_data.append(new_json)

        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(all_data, file, ensure_ascii=False, indent=4)
