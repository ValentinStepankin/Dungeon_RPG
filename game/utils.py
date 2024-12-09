import random
import json

from entities.player import Player
from entities.enemy import Enemy


def load_game_data(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Ошибка: Файл {filename} не найден.")
        exit()
    except json.JSONDecodeError:
        print(f"Ошибка: Некорректный формат файла {filename}.")
        exit()


def create_player(player_data):
    return Player(
        name=random.choice(player_data['name']),
        description=random.choice(player_data['description']),
        health=player_data['health'],
        weapon=player_data['weapon'],
        armor=player_data['armor'],
        death_description=random.choice(player_data['death_description'])
    )


def create_enemy(enemy_data):
    enemy_info = random.choice(enemy_data)
    return Enemy(
        name=enemy_info['name'],
        description=enemy_info['description'],
        health=enemy_info['health'],
        weapon=None,
        armor=None,
        death_description=enemy_info['death_description']
    )


def generate_room_descriptions(data, dungeon):
    return {i: random.choice(data['rooms']) for i in range(len(dungeon))}


def generate_enemies(dungeon, enemy_data):
    return {
        index: create_enemy(enemy_data)
        for index, room in enumerate(dungeon)
        if room == 'E'
    }


def display_room_info(current_room, dungeon, room_descriptions, enemies):
    room_type = dungeon[current_room]
    print(f"\nВы находитесь в комнате {current_room + 1}")
    print(f"Перед вами: {room_descriptions[current_room]}")
    if room_type == 'E' and current_room in enemies:
        enemy = enemies[current_room]
        print(f"Здесь находится враг: {enemy.name}. {enemy.description}")


def get_user_choice(actions):
    while True:
        print("\nВы можете:")
        for i, action in enumerate(actions, 1):
            print(f"{i}. {action}")
        choice = input("\nВаши действия: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(actions):
            return actions[int(choice) - 1]
        print("Неверный выбор. Попробуйте снова.")
