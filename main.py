import os
from src.get_vacancies import HHruAPI, CreateJson
from src.vacancies import Vacancies
from src.utils import sort_by_salary



def user_interaction():
    search_query = input("Введите наименование специальности для запроса: ")
    search_salary = input("Введите минимальную зарплату для запроса: ")
    search_sity = input("Введите город для запроса: ")
    hh = HHruAPI()
    hh.connect()
    vacancies = hh.load_vacancies(f"{search_query} {search_sity} зарплата от {search_salary}")
    cj = CreateJson('data/vacancies.json')
    cj.write(vacancies)
    path_to_file = os.path.abspath('data/vacancies.json')
    vacancies_per_salary = sort_by_salary(path_to_file)
    for i in vacancies_per_salary:
        print(i.__str__())

if __name__ == "__main__":
    user_interaction()