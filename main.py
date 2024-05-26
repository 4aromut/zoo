class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        pass


class Bird(Animal):
    def __init__(self, name, age, species):
        super().__init__(name, age)
        self.species = species

    def make_sound(self):
        return "Chirp Chirp"

    def eat(self):
        return f"{self.name} the bird is eating seeds"


class Mammal(Animal):
    def __init__(self, name, age, species):
        super().__init__(name, age)
        self.species = species

    def make_sound(self):
        return "Roar"

    def eat(self):
        return f"{self.name} the mammal is eating grass"


class Reptile(Animal):
    def __init__(self, name, age, species):
        super().__init__(name, age)
        self.species = species

    def make_sound(self):
        return "Hiss"

    def eat(self):
        return f"{self.name} the reptile is eating insects"


def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())


class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, staff):
        self.staff.append(staff)


class ZooKeeper:
    def feed_animal(self, animal):
        return f"The ZooKeeper is feeding {animal.name}"


class Veterinarian:
    def heal_animal(self, animal):
        return f"The Veterinarian is healing {animal.name}"


# Пример использования
bird1 = Bird("Parrot", 5, "Parrot species")
mammal1 = Mammal("Lion", 10, "Lion species")
reptile1 = Reptile("Snake", 3, "Snake species")

zookeeper = ZooKeeper()
veterinarian = Veterinarian()

zoo = Zoo()
zoo.add_animal(bird1)
zoo.add_animal(mammal1)
zoo.add_animal(reptile1)
zoo.add_staff(zookeeper)
zoo.add_staff(veterinarian)

animal_sound(zoo.animals)

print(zookeeper.feed_animal(bird1))
print(veterinarian.heal_animal(mammal1))




