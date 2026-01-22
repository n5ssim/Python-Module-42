"""Specialized plant types with inheritance."""


class Plant:
    """Base class for all plants."""

    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    """Inheritance from Plants."""

    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        """Make the flower bloom."""
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    """Inheritance from Plants."""

    def __init__(self, name, height, age, trunk_diameter, shade):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.shade = shade

    def produce_shade(self):
        """Make the tree expand."""
        print(
            f"{self.name} provides {self.shade} "
            f"square meters of shade"
        )


class Vegetable(Plant):
    """Inheritance from Plants."""

    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show_nutrition(self):
        """Show vitamin"""
        print(f"{self.name} is rich in {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")
    rose = Flower("Rose", 25, 30, "red")
    oak = Tree("Oak", 500, 1825, 50, 78)
    sunflower = Flower("Sunflower", 80, 45, "yellow")
    spruce = Tree("Spruce", 200, 365, 30, 58)
    carrot = Vegetable("Carrot", 20, 60, "fall", "vitamin A")
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    print(
        f"{rose.name} (Flower): {rose.height}cm, "
        f"{rose.age} days, {rose.color} color"
    )
    rose.bloom()
    print(
        f"\n{oak.name} (Tree): {oak.height}cm, "
        f"{oak.age} days, {oak.trunk_diameter}cm diameter"
    )
    oak.produce_shade()
    print(
        f"\n{tomato.name} (Vegetable): {tomato.height}cm, "
        f"{tomato.age} days, {tomato.harvest_season} harvest"
    )
    tomato.show_nutrition()
