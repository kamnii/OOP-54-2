class Hero:

    def __init__(self, name="John Doe", lvl=1, hp=100):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        print(f"self {self}")
        print(f'Базовое действие {self.name}')

    def second_method(self):
        print('Second method')

kirito = Hero("Kirito", 100, 1000)
asuna = Hero(hp=1000, name="Asuna", lvl=98)

# test = int()



kirito.action()
asuna.action()

print(asuna.hp)
