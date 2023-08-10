"""
Создайте три отдельных классов животных. У каждого класса должны быть как общие свойства, например имя, так и специфичные
Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.
Вынесите общие свойства и методы классов в класс Животное. Остальные классы наследуйте от него.
Создайте класс-фабрику который принимает тип животного (название одного из созданных классов) и параметры для этого типа.
Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
"""


class Animal:
    def __init__(self, name):
        self.name = name


class Cat(Animal):
    def show_info(self):
        print(f"Кошка по имени {self.name}")


class Dog(Animal):
    def show_info(self):
        print(f"Собака по имени {self.name}")


class Bird(Animal):
    def show_info(self):
        print(f"Птица по имени {self.name}")


class AnimalFactory:
    def create_animal(self, animal_type, name):
        if animal_type == "Cat":
            return Cat(name)
        elif animal_type == "Dog":
            return Dog(name)
        elif animal_type == "Bird":
            return Bird(name)
        else:
            return None


factory = AnimalFactory()

animal1 = factory.create_animal("Cat", "Мурзик")
animal1.show_info()

animal2 = factory.create_animal("Dog", "Шарик")
animal2.show_info()

animal3 = factory.create_animal("Bird", "Чижик")
animal3.show_info()