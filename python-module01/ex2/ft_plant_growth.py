"""Plant growth simulator."""


class Plant:
    """Represent a plant."""

    def __init__(self, name, height, age):
        """Initialize a plant."""
        self.name = name
        self.height = height
        self._age = age

    def grow(self):
        """Increase plant height by 1cm."""
        self.height += 1

    def age(self):
        """Increase plant age by one day."""
        self._age += 1

    def get_info(self):
        """Display plant information."""
        print(f"{self.name}: {self.height}cm, {self._age} days old")


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    i = 0
    print("day 1:")
    rose.get_info()
    while i < 6:
        rose.grow()
        rose.age()
        i += 1
    print("day 7:")
    rose.get_info()
    print(f"Growth this week: +{i}cm")
