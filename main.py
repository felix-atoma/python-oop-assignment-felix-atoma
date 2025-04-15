# Assignment 1: Custom Class - Superhero with Encapsulation and Inheritance

class Superhero:
    def __init__(self, name, power, team):
        self.__name = name
        self.power = power
        self.team = team

    def show_abilities(self):
        print(f"{self.__name} fights evil using {self.power}!")

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name


class Mutant(Superhero):  # Inherits from Superhero
    def __init__(self, name, power, team, mutation_type):
        super().__init__(name, power, team)
        self.mutation_type = mutation_type

    def show_abilities(self):
        print(f"{self.get_name()} has a mutation: {self.mutation_type} and uses {self.power}!")


# Test the classes
if __name__ == "__main__":
    hero = Superhero("Superman", "Flight", "Justice League")
    hero.show_abilities()

    mutant = Mutant("Wolverine", "Regeneration", "X-Men", "Adamantium Claws")
    mutant.show_abilities()

# Add Polymorphism
print("\n=== Activity 2: Polymorphism ===")

class Car:
    def move(self):
        print("Driving 🚗")

class Plane:
    def move(self):
        print("Flying ✈️")

class Boat:
    def move(self):
        print("Sailing 🚢")

# Polymorphism in action
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    vehicle.move()
