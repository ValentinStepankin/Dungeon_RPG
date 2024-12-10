import random

from game.battle import attempt_attack, calculate_damage


def test_attempt_attack():
    hit_chance = 100
    result = attempt_attack(hit_chance)
    assert result == True, f"При hit_chance = 100 результат должен быть True, получено: {result}"

    hit_chance = 0
    result = attempt_attack(hit_chance)
    assert result == False, f"При hit_chance = 0 результат должен быть False, получено: {result}"


def test_calculate_damage():
    # Тест: урон больше, чем защита
    damage = 10
    protection = 3
    result = calculate_damage(damage, protection)
    assert result == 7, f"Ожидаемый урон: 7, получено: {result}"

    # Тест: урон равен защите
    damage = 5
    protection = 5
    result = calculate_damage(damage, protection)
    assert result == 0, f"Ожидаемый урон: 0, получено: {result}"

    # Тест: урон меньше защиты
    damage = 3
    protection = 5
    result = calculate_damage(damage, protection)
    assert result == 0, f"Ожидаемый урон: 0, получено: {result}"

    # Тест: без защиты
    damage = 10
    protection = 0
    result = calculate_damage(damage, protection)
    assert result == 10, f"Ожидаемый урон: 10, получено: {result}"
