from config import DUNGEON_MAP
from game.utils import *
from game.game_actions import *


def main():
    data = load_game_data('data/dungeon.json')
    player = create_player(data['player'])
    dungeon = DUNGEON_MAP
    room_descriptions = generate_room_descriptions(data, dungeon)
    enemies = generate_enemies(dungeon, data['enemies'])

    print(f"Добро пожаловать в подземелье, {player.name}!")
    print(player.description)

    current_room = 0
    show_room_info = True

    while current_room != -1:
        if show_room_info:
            display_room_info(current_room, dungeon, room_descriptions, enemies)
        actions = get_actions(current_room, dungeon, enemies)
        action = get_user_choice(actions)

        if action == "Атаковать" and current_room in enemies:
            attack_enemy(enemies[current_room])
            del enemies[current_room]
            show_room_info = False
        else:
            show_room_info = True

        current_room = handle_action(action, current_room)


if __name__ == '__main__':
    main()
