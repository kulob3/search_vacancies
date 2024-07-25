from src.get_vacancies import HHruAPI
from src.file_worker import CreateJson
from src.utils import sort_by_salary, sort_by_date, without_sort, comparison_salary

def create_request_phrase():
    '''Функция для формирования и получения поискового запроса.'''
    search_query = input("Введите наименование специальности для запроса: ")
    search_salary = input("Введите минимальную зарплату для запроса, для поиска без учета размера зарплаты нажмите 'Enter': ")
    if not search_salary:
        search_salary = ''
    search_sity = input("Введите город для запроса, для поиска без учета города нажмите 'Enter': ")
    if not search_sity:
        search_sity = ''
    hh = HHruAPI()  # Создаем объект класса HHruAPI
    hh.connect()  # Устанавливаем соединение с HH.ru
    vacancies = hh.load_vacancies(f"{search_query} {search_sity} зарплата от {search_salary}")
    return vacancies

def made_json(vacancies):
    """Функция для создания файла json посредством создания объекта класса CreateJson"""
    cj = CreateJson()  # создаем объект класса CreateJson
    cj.write(vacancies)  # создаем json-файл для работы с вакансиями

def option_sort(change_currency_to_rub):
    """Функция для выбора действий с вакансиями"""
    vacancies_for_output = []
    while True:
        value_for_sort = input(
            "Введите '1' для сортировки по зарплате, '2' для сортировки по дате размещения, '3' для оставления вакансий с зарплатой заданного уровня, '4' - без сортировки: ")
        if value_for_sort == '1':
            vacancies_for_output = sort_by_salary(change_currency_to_rub)
            break
        elif value_for_sort == '2':
            vacancies_for_output = sort_by_date(change_currency_to_rub)
            break
        elif value_for_sort == '3':
            salary_size = int(input("Введите минимальную зарплату для сравнения: "))
            vacancies_for_output = comparison_salary(salary_size, change_currency_to_rub)
            break
        elif value_for_sort == '4':
            vacancies_for_output = without_sort(change_currency_to_rub)
            break
        else:
            print("Неверный ввод. Пожалуйста, введите '1', '2', '3' или '4'.")
    if len(vacancies_for_output) <= 20:
            for i in vacancies_for_output:
                print(i.__str__())
    else:
        batch_size = 20
        for start in range(0, len(vacancies_for_output), batch_size):
            end = start + batch_size
            for vacancy in vacancies_for_output[start:end]:
                print(vacancy.__str__())
            user_input = input("\nВведите 1, чтобы увидеть следующие вакансии или 2 для окончания просмотра: ")
            if user_input != '1':
                break





