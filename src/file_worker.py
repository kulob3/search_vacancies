from abc import ABC, abstractmethod
import os
import json
import json as js

class FileWorker(ABC):
    '''Абстрактный класс для работы с файлами'''
    @abstractmethod
    def open_file(self):
        pass

    @abstractmethod
    def delete_file(self):
        pass

class DictWorker(ABC):
    '''Абстрактный класс для работы со словарем'''
    @abstractmethod
    def write(self, data):
        pass


class CreateJson(DictWorker):
    ''' Класс для создания файла json из списка'''
    __filename = os.path.abspath('data/vacancies.json')

    @property
    def filename(self):
        return self.__filename

    @filename.setter
    def filename(self, value):
        self.__filename = value

    def write(self, data):
        '''Функция для создания директории и записи данных в файл json'''
        directory = os.path.dirname(self.filename)
        if not os.path.exists(directory):
            os.makedirs(directory)
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

class JsonWorker(FileWorker):
    '''Класс для открытия и удаления файла json'''

    __path_to_file = os.path.abspath('data/vacancies.json')

    def open_file(self):
        '''Функция для открытия файла json'''
        path_vacancies = os.path.abspath(self.path_to_file)
        with open(path_vacancies, 'r', encoding='utf-8') as file:
            list_vacancies = js.loads(file.read())
            return list_vacancies

    @property
    def path_to_file(self):
        return self.__path_to_file

    @path_to_file.setter
    def path_to_file(self, value):
        self.__path_to_file = value

    def delete_file(self):
        '''Функция для удаления файла json'''
        try:
            os.remove(self.path_to_file)
            print(f"Файл {self.__path_to_file} удален")
        except FileNotFoundError:
            print(f"Файл {self.__path_to_file} не найден")