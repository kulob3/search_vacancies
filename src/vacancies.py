from datetime import datetime



class Vacancies:
    ''' Класс для представления вакансий '''
    def __init__(self, name, employer, salary, currency, expirience, employment, area, published_at, alternate_url):
        self.name = name
        self.employer = employer
        self.salary = salary if salary else 'Не указана'
        self.currency = currency if salary else ''
        self.expirience = expirience
        self.employment = employment
        self.area = area
        self.published_at = datetime.strptime(published_at, '%Y-%m-%dT%H:%M:%S%z').strftime('%d.%m.%Y')
        self.alternate_url = alternate_url

    def __str__(self):
        return f"\n{self.name}\nРаботодатель: {self.employer}\nЗарплата от: {self.salary} {self.currency}\nТребуемый опыт: {self.expirience}\nТип занятости: {self.employment}\nГород: {self.area}\nДата размещения: {self.published_at}\n{self.alternate_url}"

