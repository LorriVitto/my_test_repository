
from abc import ABC, abstractmethod

# Создаем абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Создаем конкретные типы оружия
class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."

class Bow(Weapon):
    def attack(self):
        return "Боец стреляет из лука."

# Класс Fighter представляет бойца
class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon):
        self.weapon = weapon
        print(f"{self.name} выбирает {type(weapon).__name__.lower()}.")

    def attack(self, monster):
        if self.weapon is not None:
            print(self.weapon.attack())
            monster.defeat()
        else:
            print("Боец без оружия.")

# Класс Monster представляет монстра
class Monster:
    def __init__(self, name):
        self.name = name

    def defeat(self):
        print(f"{self.name} побежден!")

# Демонстрация боя
def main():
    fighter = Fighter("Боец")
    monster = Monster("Монстр")

    # Боец выбирает меч и атакует
    sword = Sword()
    fighter.change_weapon(sword)
    fighter.attack(monster)

    # Боец выбирает лук и атакует
    bow = Bow()
    fighter.change_weapon(bow)
    fighter.attack(monster)

if __name__ == "__main__":
    main()