class Character:
    def __init__(self, name, level, health, attack):
        self.name = name         
        self.level = level       
        self.health = health    
        self.attack = attack    

    def display_info(self):
        print(f"Ім'я: {self.name}")
        print(f"Рівень: {self.level}")
        print(f"Здоров'я: {self.health}")
        print(f"Атака: {self.attack}")

hero = Character("Артур", 5, 100, 20)
hero.display_info()
