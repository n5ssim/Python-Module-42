"""Garden security system"""


class SecurePlant:
    """Protected data"""

    def __init__(self, name: str) -> None:
        """Initialize a secure plant."""
        self.name = name
        self._height = 0
        self._age = 0
        print(f"Plant created: {name}")

    def get_height(self) -> int:
        """return height."""
        return self._height

    def get_age(self) -> int:
        """return age"""
        return self._age

    def set_height(self, value: int) -> None:
        """Error message if invalid height."""
        if value < 0:
            print(f"\nInvalid operation attempted: height {value}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = value
            print(f"Height updated: {value}cm [OK]")

    def set_age(self, value: int) -> None:
        """Error message if invalid age."""
        if value < 0:
            print(f"\nInvalid operation attempted: age {value} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = value
            print(f"Age updated: {value} days [OK]")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose")
    rose.set_height(25)
    rose.set_age(30)
    rose.set_height(-5)
    print(
        f"\nCurrent plant: {rose.name} ({rose.get_height()}cm, {rose.get_age()} days)"
    )
