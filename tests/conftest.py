import pytest

@pytest.fixture
def player_data():
    return {
        'name': ["Степан Дубина", "Цицерон Иванович", "Васька Проказник"],
        'description': [
            "Вы в расцвете сил, амбициозны, имеете крепкое телосложение. Для вас не существует никаких препятствий. Ну, кроме финансовых, с этим у вас проблемы.",
            "Вам за 50 лет, по местным меркам - глубокая старость. Но несбывшиеся мечты молодости толкают вас на авантюры.",
            "Вы сирота, живущая на улице. Единственный способ улучшить свою жизнь для вас, это найти что-то ценное в опасных и заброшенных местах."
        ],
        'health': 10,
        'weapon': {
            "name": "Опасная дубина",
            "description": "Крепкая сосновая ветка с вбитым ржавым гвоздем на конце.",
            "damage": 5,
            "hit_chance": 75
        },
        'armor': {
            "name": "Легкий кожаный доспех",
            "description": "Сшитый из крыс кожаный доспех. Пахнет ужасно, но вроде бы защищает от урона.",
            "protection": 2
        },
        'death_description': [
            "Ваша кончина была долгой и мучительной. Вы успели тысячу раз пожалеть, что ввязались во всё это...",
            "Ваша кончина была быстрой. Вы даже не поняли, как погибли."
        ]
    }


@pytest.fixture
def enemy_data():
    return [
        {
            "name": "Зомби",
            "description": "Полуразложившийся ходячий труп, который бесцельно бродит из стороны в сторону.",
            "health": 10,
            "death_description": "Зловонная туша распласталась на полу. Больше признаков жизни не подает."
        },
        {
            "name": "Пещерный гоблин",
            "description": "Мелкий безобразный гоблин. Очень хитрый и подлый.",
            "health": 8,
            "death_description": "Небольшая тушка лежит на полу в луже собственного ихора."
        },
        {
            "name": "Скелет",
            "description": "Обыкновенный бродячий костяк. Творение некромантов самоучек.",
            "health": 5,
            "death_description": "Груда костей, рассыпалась по всей комнате."
        }
    ]


@pytest.fixture
def room_data():
    return {
        "rooms": [
            "Просторная комната. Большие дубовые бочки, стоящие вдоль стен, подсказывают, что раньше тут хранили вино.",
            "Темная комната. Одна стена частично обвалилась, впустив в себя черную почву. В воздухе стоит плотный запах сырости и плесени.",
            "Комната, как комната, ничего особенного.",
            "Судя по, стоящим вдоль стен, кроватям с истлевшими простынями, раньше это были покои прислуги.",
            "Скелеты пустых оружейных стоек, расположенные вдоль правой стены, подсказывающие вам, что раньше это была оружейная."
        ]
    }