class Person:

    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def introduce(self):
        return print(f"Привет меня зовут {self.name}, мой age {self.age}, мой city {self.city}")

    def is_adult(self):
        if self.age > 17:
            return print(True)
        else:
            return print(False)

kaniet = Person("kaniet", 20, "Bishkek")
islam = Person("islam", 19, "Bishkek")
bakai = Person("bakai", 6, "Bishkek")

kaniet.introduce()
kaniet.is_adult()
islam.is_adult()
bakai.is_adult()