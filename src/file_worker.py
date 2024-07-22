from abc import ABC, abstractmethod
import os
import json as js
class FileWorker(ABC):
    @abstractmethod
    def open_file(self):
        pass

    @abstractmethod
    def delete_file(self):
        pass

class JsonWorker(FileWorker):

    __path_to_file = os.path.abspath('data/vacancies.json')
    # def __init__(self, path_to_file):
    #     self.path_to_file = path_to_file

    def open_file(self):
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
        try:
            os.remove(self.path_to_file)
            print(f"Файл {self.path_to_file} удален")
        except FileNotFoundError:
            print(f"Файл {self.path_to_file} не найден")