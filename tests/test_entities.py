import random
from entities.player import Player
from entities.enemy import Enemy


def test_player_init(player_data):
    # Случайный выбор данных игрока из фикстуры
    player_info = {
        'name': random.choice(player_data['name']),
        'description': random.choice(player_data['description']),
        'health': player_data['health'],
        'weapon': player_data['weapon'],
        'armor': player_data['armor'],
        'death_description': random.choice(player_data['death_description'])
    }

    player = Player(
        player_info['name'],
        player_info['description'],
        player_info['health'],
        player_info['weapon'],
        player_info['armor'],
        player_info['death_description']
    )

    # Проверяем основные атрибуты игрока
    assert player.name == player_info['name']
    assert player.description == player_info['description']
    assert player.health == player_info['health']

    # Проверяем параметры оружия
    assert player.weapon == player_info['weapon']
    assert player.weapon['name'] == player_info['weapon']['name']
    assert player.weapon['damage'] == player_info['weapon']['damage']
    assert player.weapon['hit_chance'] == player_info['weapon']['hit_chance']

    # Проверяем параметры брони
    assert player.armor == player_info['armor']
    assert player.armor['name'] == player_info['armor']['name']
    assert player.armor['protection'] == player_info['armor']['protection']

    # Проверяем описание смерти
    assert player.death_description == player_info['death_description']


def test_enemy_init(enemy_data, weapon_data, armor_data):
    # Случайный выбор врага из фикстуры
    enemy_info = random.choice(enemy_data)
    weapon_info = random.choice(weapon_data)
    armor_info = random.choice(armor_data)

    enemy = Enemy(
        enemy_info['name'],
        enemy_info['description'],
        enemy_info['health'],
        weapon_info,
        armor_info,
        enemy_info['death_description']
    )

    # Проверяем основные атрибуты врага
    assert enemy.name == enemy_info['name']
    assert enemy.description == enemy_info['description']
    assert enemy.health == enemy_info['health']

    # Проверяем оружие врага
    assert enemy.weapon['name'] == weapon_info['name']
    assert enemy.weapon['description'] == weapon_info['description']
    assert enemy.weapon['damage'] == weapon_info['damage']
    assert enemy.weapon['hit_chance'] == weapon_info['hit_chance']

    # Проверяем броню врага
    assert enemy.armor['name'] == armor_info['name']
    assert enemy.armor['description'] == armor_info['description']
    assert enemy.armor['protection'] == armor_info['protection']

    # Проверяем описание смерти
    assert enemy.death_description == enemy_info['death_description']

