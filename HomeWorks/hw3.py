class Student:

    def __init__(self, name, grade):
        self.__name = name
        self.__grade = grade

    def set_grade(self, new_grade):
        if 0 <= self.__grade <= 100:
            self.__grade = new_grade
            return self.__grade
        else:
            return print('Неправильная оценка')

    def get_grade(self):
        return self.__grade

    def get_info(self):
        return print(f'Имя {self.__name}, Оценка {self.__grade}')


class Shape:

    def area(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Square(Shape):

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side
