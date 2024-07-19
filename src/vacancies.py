from datetime import datetime



class Vacancies:
    ''' Класс для представления вакансий '''
    def __init__(self, name, employer, salary, currency, expirience, employment, area, published_at, alternate_url):
        self.name = name if name else 'Не указано'
        self.employer = employer if employer else 'Не указан'
        self.salary = salary if salary else 'Не указана'
        self.currency = currency if salary else ''
        self.expirience = expirience if expirience else 'Не указан'
        self.employment = employment if employment else 'Не указан'
        self.area = area if area else 'Не указан'
        self.published_at = datetime.strptime(published_at, '%Y-%m-%dT%H:%M:%S%z').strftime('%d.%m.%Y') if published_at else 'Не указана'
        self.alternate_url = alternate_url if alternate_url else 'Не указан'

    def __str__(self):
        return f"\n{self.name}\nРаботодатель: {self.employer}\nЗарплата от: {self.salary} {self.currency}\nТребуемый опыт: {self.expirience}\nТип занятости: {self.employment}\nГород: {self.area}\nДата размещения: {self.published_at}\n{self.alternate_url}"

    def __lt__(self, other):
        if not isinstance(other, Vacancies):
            return NotImplemented
        try:
            return int(self.salary) < int(other.salary)
        except ValueError:
            # Handle the case where salary cannot be converted to int
            raise TypeError("Salary comparison is invalid due to non-integer values.")



if __name__ == "__main__":
    v = Vacancies('Python developer', 'Company', 100000, 'RUB', '1 year', 'full-time', 'Moscow', '2021-09-01T00:00:00+0300', 'https://hh.ru')
    v1 = Vacancies('Python developer', 'Company', None, 'RUB', '1 year', 'full-time', 'Moscow', '2021-09-01T00:00:00+0300', '1')
    print(v.__str__())
    print(v1.__str__())
    print(v < v1)
