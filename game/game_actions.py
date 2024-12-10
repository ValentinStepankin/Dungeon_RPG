
def get_actions(current_room, dungeon, enemies):
    actions = []
    room_type = dungeon[current_room]

    if current_room > 0:
        actions.append("Вернуться назад")
    if current_room < len(dungeon) - 1 and (room_type != 'E' or current_room not in enemies):
        actions.append("Пойти дальше")
    if room_type == 'E' and current_room in enemies:
        actions.append("Атаковать")
    if room_type == 'Ex':
        actions.append("Выйти из подземелья")
    return actions


def handle_action(action, current_room):
    if action == "Вернуться назад":
        return current_room - 1
    elif action == "Пойти дальше":
        return current_room + 1
    elif action == "Выйти из подземелья":
        print("Вы успешно вышли из подземелья. Конец игры.")
        return -1
    return current_room
