"""Garden analytics platform with nested components and inheritance."""


class Plant:
    """Base class for all plants."""

    def __init__(self, name: str, height: int) -> None:
        """initialize a plant with name and height."""
        self.name = name
        self.height = height

    def grow(self) -> None:
        """Make the plant grow by 1cm"""
        self.height += 1
        print(f"{self.name} grew 1cm")

    def __str__(self) -> str:
        """String representation of the plant."""
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    """Plant that can produce flowers - inherits from Plant."""

    def __init__(self, name: str, height: int, flower_color: str) -> None:
        """Initialize a flowering plant."""
        super().__init__(name, height)
        self.flower_color = flower_color
        self.is_blooming: bool = True

    def __str__(self) -> str:
        """String representation with flower info."""
        bloom_status = "blooming" if self.is_blooming else "not blooming"
        return (f"{self.name}: {self.height}cm, "
                f"{self.flower_color} flowers ({bloom_status})")


class PrizeFlower(FloweringPlant):
    """Prize-winning flower - inherits from FloweringPlant."""

    def __init__(self, name: str, height: int, flower_color: str,
                 prize_points: int) -> None:
        """Initialize a prize flower."""
        super().__init__(name, height, flower_color)
        self.prize_points = prize_points

    def __str__(self) -> str:
        """String representation with prize info."""
        base_str = super().__str__()
        return f"{base_str}, Prize points: {self.prize_points}"


class GardenManager:
    """Manages gardens with comprehensive analytics capabilities."""

    total_gardens: int = 0

    class GardenStats:
        """Nested helper class for calculating garden statistics."""

        def __init__(self, plants: list[Plant]) -> None:
            """Initialize stats calculator with plant list."""
            self.plants = plants

        def count_by_type(self) -> tuple[int, int, int]:
            """Count plants by type: (regular, flowering, prize)."""
            regular = 0
            flowering = 0
            prize = 0

            for plant in self.plants:
                if isinstance(plant, PrizeFlower):
                    prize += 1
                elif isinstance(plant, FloweringPlant):
                    flowering += 1
                else:
                    regular += 1

            return regular, flowering, prize

        def total_height(self) -> int:
            """Calculate total height of all plants."""
            return sum(plant.height for plant in self.plants)

    def __init__(self, owner_name: str) -> None:
        """Initialize a garden manager for one owner."""
        self.owner_name = owner_name
        self.plants: list[Plant] = []
        self.total_growth: int = 0
        GardenManager.total_gardens += 1

    def add_plant(self, plant: Plant, silent: bool = False) -> None:
        """Add a plant to this garden (instance method)."""
        self.plants.append(plant)
        if not silent:
            print(f"Added {plant.name} to {self.owner_name}'s garden")

    def grow_all(self) -> None:
        """Make all plants in this garden grow (instance method)."""
        print(f"{self.owner_name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.total_growth += 1

    def get_report(self) -> None:
        """Generate a detailed report for this garden (instance method)."""
        print(f"\n=== {self.owner_name}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(f"- {plant}")

        stats = self.GardenStats(self.plants)
        regular, flowering, prize = stats.count_by_type()

        print(f"\nPlants added: {len(self.plants)}, "
              f"Total growth: {self.total_growth}cm")
        print(f"Plant types: {regular} regular, "
              f"{flowering} flowering, {prize} prize flowers")

    def calculate_score(self) -> int:
        """Calculate garden score based on height and bonuses."""
        score = 0
        for plant in self.plants:
            score += plant.height
            if isinstance(plant, PrizeFlower):
                score += 40
            elif isinstance(plant, FloweringPlant):
                score += 30
        return score

    @classmethod
    def create_garden_network(cls) -> tuple["GardenManager", "GardenManager"]:
        """Create multiple garden managers at once (class method)."""
        alice_garden = cls("Alice")
        bob_garden = cls("Bob")
        return alice_garden, bob_garden

    @staticmethod
    def validate_height(height: int) -> bool:
        """Validate if a height value is acceptable (static method)."""
        return height > 0 and height < 1000


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    alice, bob = GardenManager.create_garden_network()

    alice.add_plant(Plant("Oak Tree", 100))
    alice.add_plant(FloweringPlant("Rose", 25, "red"))
    alice.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))
    bob.add_plant(Plant("Maple", 42), silent=True)
    bob.add_plant(FloweringPlant("Tulip", 20, "pink"), silent=True)

    print()
    alice.grow_all()

    alice.get_report()

    print(f"\nHeight validation test: {GardenManager.validate_height(50)}")

    alice_score = alice.calculate_score()
    bob_score = bob.calculate_score()
    print(f"Garden scores - Alice: {alice_score}, Bob: {bob_score}")

    print(f"Total gardens managed: {GardenManager.total_gardens}")
