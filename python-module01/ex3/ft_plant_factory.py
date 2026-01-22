"""Plant factory"""


class Plant:
    """Represents a plant."""

    def __init__(self, name, height, age):
        """Initialize a plant."""
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    plants = []
    plants.append(Plant("Rose", 25, 30))
    plants.append(Plant("Oak", 200, 365))
    plants.append(Plant("Cactus", 5, 90))
    plants.append(Plant("Sunflower", 80, 45))
    plants.append(Plant("Fern", 15, 120))
    for plant in plants:
        print(f"Created: {plant.name} ({plant.height}cm, {plant.age} days)")
    print(f"\nTotal plants created: {len(plants)}")
