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
        print("-" * 20)

    def attack_enemy(self, enemy):
        if self.health <= 0:
            print(f"{self.name} не може атакувати — він переможений.")
            return
        if enemy.health <= 0:
            print(f"{enemy.name} вже переможений.")
            return

        print(f"{self.name} атакує {enemy.name} на {self.attack} одиниць!")
        enemy.health -= self.attack
        if enemy.health <= 0:
            enemy.health = 0
            print(f"{enemy.name} переможений!")
        else:
            print(f"У {enemy.name} залишилось {enemy.health} здоров’я.")

hero1 = Character("Артур", 5, 100, 25)
hero2 = Character("Моргана", 4, 90, 20)

hero1.display_info()
hero2.display_info()

hero1.attack_enemy(hero2)
hero2.attack_enemy(hero1)
hero1.attack_enemy(hero2)
hero1.attack_enemy(hero2)

hero1.display_info()
hero2.display_info()
