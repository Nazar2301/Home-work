class Animal:
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        if isinstance(food, Plant) and food.edible:
            print(f"{self.name} съел {food.name}")
            Animal.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            Animal.alive = False

class Plant:
    edible = False

    def __init__(self, name):
        self.name = name

class Mammal(Animal):
    pass

class Predator(Animal):
    pass

class Flower(Plant):
    pass

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        Plant.edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(Animal.alive)
print(Animal.fed)
a1.eat(p1)
a2.eat(p2)
print(Animal.alive)
print(Animal.fed)
