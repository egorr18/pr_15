class Character:
    def __init__(self, name, level, health, attack):
        self.name = name
        self.level = level
        self.health = health
        self.attack = attack

    def display_info(self):
        print(f"Ім'я: {self.name}")
        print(f"Клас: {self.__class__.__name__}")
        print(f"Рівень: {self.level}")
        print(f"Здоров'я: {self.health}")
        print(f"Атака: {self.attack}")

    def restore_health(self, amount):
        self.health += amount
        print(f"{self.name} відновив(ла) {amount} HP. Поточне здоров’я: {self.health}")


class Warrior(Character):
    def __init__(self, name, level, health, attack, armor):
        super().__init__(name, level, health, attack)
        self.armor = armor  

    def display_info(self):
        super().display_info()
        print(f"Броня: {self.armor}")
        print("-" * 20)


class Mage(Character):
    def __init__(self, name, level, health, attack, mana):
        super().__init__(name, level, health, attack)
        self.mana = mana  

    def display_info(self):
        super().display_info()
        print(f"Мана: {self.mana}")
        print("-" * 20)


class Archer(Character):
    def __init__(self, name, level, health, attack, arrows):
        super().__init__(name, level, health, attack)
        self.arrows = arrows

    def display_info(self):
        super().display_info()
        print(f"Стріли: {self.arrows}")
        print("-" * 20)

w = Warrior("Бальтазар", 7, 120, 30, armor=50)
m = Mage("Мерлін", 10, 80, 40, mana=100)
a = Archer("Робін", 6, 90, 25, arrows=15)

w.display_info()
m.display_info()
a.display_info()

w.restore_health(20)
m.restore_health(30)
a.restore_health(15)
