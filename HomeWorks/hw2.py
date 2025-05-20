import random

class Heroes:

    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def action(self):
        return print('Some action')

    def attack(self):
        return print("Some attack")


class Archer(Heroes):

    def __init__(self, name, hp, arrows, precision):
        super().__init__(name, hp)
        self.arrows = arrows
        self.precision = precision

    def attack(self):
        a = random.randint(1, 100)
        if self.arrows > 0:
            if a <= self.precision:
                self.arrows -= 1
                return print("Есть попадание!\n")
            else:
                self.arrows -= 1
                return print('Промах\n')
        else:
            return print("У вас нет стрел, пополните их командой \"rest\"\n")

    def rest(self):
        self.arrows += 5
        return print('Добавлено 5 стрел\n')

    def status(self):
        return print(f'Данные о персонаже:\n'
                     f'Имя: {self.name}\n'
                     f'Здоровье: {self.hp}\n'
                     f'Количество стрел: {self.arrows}\n'
                     f'Точность: {self.precision}\n')

isida = Archer("Uriu", 560, 5, 80)

isida.attack()
isida.attack()
isida.attack()
isida.attack()
isida.attack()
isida.attack()
isida.rest()
isida.attack()
isida.attack()
isida.attack()
isida.status()
