import random


def attack_enemy(player, enemy):
    max_health_enemy = enemy.health
    max_health_player = player.health

    display_health(player.name, player.health, max_health_player)
    display_health(enemy.name, enemy.health, max_health_enemy)

    print(f"Вы решительно бросаетесь на противника. Завязался бой:")

    while player.health > 0 and enemy.health > 0:
        # Игрок атакует
        print("\nВы наносите удар!")
        if attempt_attack(player.weapon['hit_chance']):
            damage = calculate_damage(player.weapon['damage'], enemy.armor['protection'] if enemy.armor else 0)
            enemy.health = max(0, enemy.health - damage)
            print(f"Удар пришёлся точно в цель! Вы нанесли {damage} урона цели {enemy.name}.")
        else:
            print(f"{enemy.name} смог увернуться от вашего удара.")

        display_health(enemy.name, enemy.health, max_health_enemy)

        # Проверяем, жив ли противник
        if enemy.health <= 0:
            print(f"\nВы одержали победу над {enemy.name}! {enemy.death_description}")
            break

        # Противник атакует
        print(f"\n{enemy.name} наносит ответный удар. Берегитесь!")
        if attempt_attack(enemy.weapon['hit_chance'] if enemy.weapon else 10):
            damage = calculate_damage(enemy.weapon['damage'] if enemy.weapon else 1, player.armor['protection'])
            player.health = max(0, player.health - damage)
            print(f"На этот раз вы не смогли увернуться... Противник нанёс вам {damage} урона.")
        else:
            print(f"Удар был внезапным, но вы смогли увернуться. Оружие пролетело в сантиметре от вашего лица.")

        display_health(player.name, player.health, max_health_player)

        # Проверяем, жив ли игрок
        if player.health <= 0:
            print(f"\n{player.death_description}")
            return False
    return True


def attempt_attack(hit_chance):
    return random.randint(0, 100) <= hit_chance


def calculate_damage(weapon_damage, armor_protection):
    return max(0, weapon_damage - armor_protection)


def display_health(name, current_health, max_health):
    health_bar = "▋" * current_health + "_" * (max_health - current_health)
    print(f"Состояние здоровья у {name}: {current_health}/{max_health}")
    print(f"|{health_bar}|")
