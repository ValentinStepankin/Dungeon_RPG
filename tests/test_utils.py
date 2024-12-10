import os
from game.utils import load_game_data, create_player, create_enemy, generate_room_descriptions, generate_enemies

def test_load_game_data_success():
    # Проверяем успешную загрузку данных из json файла
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, '../data/dungeon.json')
    file_path = os.path.abspath(file_path)

    data = load_game_data(file_path)
    assert isinstance(data, dict), "Данные должны быть в формате словаря."
    assert 'player' in data, "Отсутствуют данные о игроке."
    assert 'enemies' in data, "Отсутствуют данные о врагах."
    assert 'weapon' in data, "Отсутствуют данные об оружии."
    assert 'armor' in data, "Отсутствуют данные о доспехах."
    assert 'rooms' in data, "Отсутствуют данные о комнатах."


def test_create_player(player_data):
    # Проверка правильности создания игрока с помощью функции create_player
    player = create_player(player_data)
    assert player.name in player_data['name'], f"Имя игрока должно быть одно из: {player_data['name']}"
    assert player.description in player_data['description'], f"Описание игрока должно быть одно из: {player_data['description']}"
    assert player.health == player_data['health'], f"Здоровье игрока должно быть {player_data['health']}"
    assert player.weapon['name'] == player_data['weapon']['name'], f"Оружие игрока должно быть '{player_data['weapon']['name']}'"
    assert player.weapon['description'] == player_data['weapon']['description'], f"Описание оружия должно быть '{player_data['weapon']['description']}'"
    assert player.weapon['damage'] == player_data['weapon']['damage'], f"Урон оружия должен быть {player_data['weapon']['damage']}"
    assert player.weapon['hit_chance'] == player_data['weapon']['hit_chance'], f"Шанс попадания оружия должен быть {player_data['weapon']['hit_chance']}"
    assert player.armor['name'] == player_data['armor']['name'], f"Броня игрока должна быть '{player_data['armor']['name']}'"
    assert player.armor['description'] == player_data['armor']['description'], f"Описание брони должно быть '{player_data['armor']['description']}'"
    assert player.armor['protection'] == player_data['armor']['protection'], f"Защита брони должна быть {player_data['armor']['protection']}"
    assert player.death_description in player_data['death_description'], f"Описание смерти игрока должно быть одно из: {player_data['death_description']}"


def test_create_enemy(enemy_data, weapon_data, armor_data):
    # Проверка правильности создания противника с помощью функции create_enemy
    enemy = create_enemy(enemy_data, weapon_data, armor_data)

    # Проверка, что имя врага соответствует одному из возможных
    assert enemy.name in [enemy_data[0]['name'], enemy_data[1]['name'], enemy_data[2]['name']], \
        f"Имя врага должно быть одно из: {', '.join([enemy_data[0]['name'], enemy_data[1]['name'], enemy_data[2]['name']])}"

    # Проверка, что описание врага соответствует одному из возможных
    assert enemy.description in [enemy_data[0]['description'], enemy_data[1]['description'],
                                 enemy_data[2]['description']], \
        f"Описание врага должно быть одно из: {', '.join([enemy_data[0]['description'], enemy_data[1]['description'], enemy_data[2]['description']])}"

    # Проверка, что здоровье врага соответствует одному из возможных
    assert enemy.health in [enemy_data[0]['health'], enemy_data[1]['health'], enemy_data[2]['health']], \
        f"Здоровье врага должно быть одно из: {enemy_data[0]['health']}, {enemy_data[1]['health']}, {enemy_data[2]['health']}"

    # Проверка, что описание смерти врага соответствует одному из возможных
    assert enemy.death_description in [enemy_data[0]['death_description'], enemy_data[1]['death_description'],
                                       enemy_data[2]['death_description']], \
        f"Описание смерти врага должно быть одно из: {', '.join([enemy_data[0]['death_description'], enemy_data[1]['death_description'], enemy_data[2]['death_description']])}"

    # Проверка оружия врага
    assert enemy.weapon['name'] in [weapon['name'] for weapon in weapon_data], \
        f"Оружие врага должно быть одно из: {', '.join([weapon['name'] for weapon in weapon_data])}"
    assert enemy.weapon['damage'] in [weapon['damage'] for weapon in weapon_data], \
        f"Урон оружия врага должен быть один из: {', '.join([str(weapon['damage']) for weapon in weapon_data])}"
    assert enemy.weapon['hit_chance'] in [weapon['hit_chance'] for weapon in weapon_data], \
        f"Шанс попадания оружия врага должен быть один из: {', '.join([str(weapon['hit_chance']) for weapon in weapon_data])}"

    # Проверка брони врага
    assert enemy.armor['name'] in [armor['name'] for armor in armor_data], \
        f"Броня врага должна быть одно из: {', '.join([armor['name'] for armor in armor_data])}"
    assert enemy.armor['protection'] in [armor['protection'] for armor in armor_data], \
        f"Защита брони врага должна быть одна из: {', '.join([str(armor['protection']) for armor in armor_data])}"


def test_generate_room_descriptions(room_data):
    # Проверка корректности описаний комнат

    dungeon = ['St', ' ', 'E', 'Ex']
    room_descriptions = generate_room_descriptions(room_data, dungeon)
    assert len(room_descriptions) == len(
        dungeon), f"Количество описаний комнат должно быть равно количеству комнат. Ожидалось {len(dungeon)}, но получено {len(room_descriptions)}."

    valid_descriptions = room_data['rooms']
    for description in room_descriptions.values():
        assert description in valid_descriptions, f"Описание комнаты '{description}' не найдено в списке допустимых описаний."


def test_generate_enemies(enemy_data, weapon_data, armor_data):
    # Проверка генерации врагов для комнат 'E'
    dungeon = ['St', 'E',' ', 'E', 'Ex']
    enemies = generate_enemies(dungeon, enemy_data, weapon_data, armor_data)
    assert len(enemies) == 2, "Количество врагов должно быть 2"
    expected_enemy_indices = [1, 3]
    assert list(enemies.keys()) == expected_enemy_indices, f"Враги должны быть созданы только для комнат с индексами {expected_enemy_indices}"
