class Country:
    def __init__(self, name, population, area, gdp, currency, language, capital, region):
        self.name = name
        self.population = population
        self.area = area
        self.gdp = gdp
        self.currency = currency
        self.language = language
        self.capital = capital
        self.region = region
        self.counties = []  # Список округов
        self.budget = 33000000  # Бюджет страны

    def add_county(self, county):
        self.counties.append(county)

    def collect_taxes(self):
        total_taxes = 0
        for county in self.counties:
            total_taxes += county.collect_taxes()
        self.budget += total_taxes
        print(f"Taxes collected, current country budget: {self.budget}.")

    def get_budget(self):
        return self.budget

    def get_info(self):
        return {
            "name": self.name,
            "population": self.population,
            "area": self.area,
            "gdp": self.gdp,
            "currency": self.currency,
            "language": self.language,
            "capital": self.capital,
            "region": self.region,
            "budget": self.budget
        }


class County:
    def __init__(self, name, population, area, gdp):
        self.name = name
        self.population = population
        self.area = area
        self.gdp = gdp
        self.cities = []  # Список городов
        self.budget = 0  # Бюджет округа

    def add_city(self, city):
        self.cities.append(city)

    def process_city_request(self, city, amount):
        if self.budget >= amount:
            self.budget -= amount
            city.receive_funding(amount)
            print(f"City's request {city.name} for financing is accepted.")
        else:
            print(f"District's budget {self.name} isn't enough to satisfy city {city.name}'s request.")

    def collect_taxes(self):
        total_taxes = 0
        for city in self.cities:
            total_taxes += city.collect_taxes()
        self.budget += total_taxes
        print(f"Taxes collected in district {self.name}, current district budget: {self.budget}.")
        return total_taxes

    def get_budget(self):
        return self.budget

    def get_info(self):
        return {
            "name": self.name,
            "population": self.population,
            "area": self.area,
            "gdp": self.gdp,
            "budget": self.budget,
            "cities_count": len(self.cities)
        }


class City:
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area
        self.budget = 0  # Бюджет города
        self.residents = []  # Список жителей

    def request_funding(self, amount):
        print(f"City {self.name} requests financing in the amount of {amount}.")
        # Запрашиваем финансирование у округа
        for county in self.city.counties:  # Тут мы обращаемся к округу города
            county.process_city_request(self, amount)

    def receive_funding(self, amount):
        self.budget += amount
        print(f"City {self.name} received {amount} of financing, current city budget: {self.budget}.")

    def collect_taxes(self):
        total_taxes = 0
        for resident in self.residents:
            total_taxes += resident.pay_taxes()
        self.budget += total_taxes
        print(f"Taxes collected in city {self.name}, current city budget: {self.budget}.")
        return total_taxes

    def add_resident(self, person):
        self.residents.append(person)
        print(f"Resident {person.name} added to city {self.name}.")

    def remove_resident(self, person):
        self.residents.remove(person)
        print(f"Resident {person.name} removed from city {self.name}.")

    def get_info(self):
        return {
            "name": self.name,
            "population": self.population,
            "area": self.area,
            "budget": self.budget,
            "residents_count": len(self.residents)
        }


class Person:
    def __init__(self, name, age, income, city=None):
        self.name = name
        self.age = age
        self.income = income
        self.city = city
        if city:
            city.add_resident(self)

    def pay_taxes(self):
        tax = self.income * 0.2  # Платит 20% от дохода
        print(f"{self.name} pays taxes in the amount of {tax}.")
        return tax

    def move_to_city(self, new_city):
        if self.city:
            self.city.remove_resident(self)
        self.city = new_city
        new_city.add_resident(self)
        print(f"{self.name} relocated to city {new_city.name}.")

    def get_info(self):
        return {
            "name": self.name,
            "age": self.age,
            "income": self.income,
            "city": self.city.name if self.city else "None"
        }


country = Country("Estonia", 1326535, 45227, 50000, "Euro", "Estonian", "Tallinn", "Northern Europe")
country = Country("France", 68521974, 45227445, 50000554, "Euro", "French", "Paris", "Western Europe")
county_1 = County("Harjumaa", 600000, 5000, 10000)
county_2 = County("Saaremaa", 30000, 2000, 2000)
county_3 = County("Ida-Virumaa", 150000, 4000, 5000)
county_4 = County("Pärnumaa", 130000, 5000, 6000)

country.add_county(county_1)
country.add_county(county_2)
country.add_county(county_3)
country.add_county(county_4)

city_1 = City("Tallinn", 405000, 5000)
city_2 = City("Hapsalu", 11000, 100)
city_3 = City("Saaremaa", 7000, 150)
city_4 = City("Tartu", 100000, 200)
city_5 = City("Narva", 12203, 300)

county_1.add_city(city_1)
county_2.add_city(city_2)
county_3.add_city(city_3)
county_4.add_city(city_4)
county_4.add_city(city_5)

person_1 = Person("Faust", 35, 50000, city_1)
person_2 = Person("Yharim", 40, 55000, city_4)
person_3 = Person("Jack", 29, 45000, city_2)
person_4 = Person("Hastur", 100, 60000, city_3)
person_5 = Person("Valentine", 38, 70000, city_4)

# Перемещаем жителей
print("\nRelocation of Residents:")
person_1.move_to_city(city_1)  # Faust перемещается из Таллина в Хаапсалу
person_2.move_to_city(city_5)  # Yharim перемещается из Тарту в Нарву

# Собираем налоги с городов и округов
country.collect_taxes()

# Выводим информацию о бюджете страны, округов и городов
print("\nCountry Info:")
print(country.get_info())

print("\nCounty Info:")
for county in country.counties:
    print(county.get_info())

print("\nCity Info:")
for county in country.counties:
    for city in county.cities:
        print(city.get_info())

print("\nPeople Info:")
for person in [person_1, person_2, person_3, person_4, person_5]:
    print(person.get_info())
