from random import randint

from graphic_arts.start_game_banner import run_screensaver


def attack(char_name: str,
           char_class: str) -> str:
    """Вычисляет количество атаки персонажа."""
    if char_class == 'warrior':
        ataka_w: int = 5 + randint(3, 5)
        return (f'{char_name} нанёс урон противнику равный {ataka_w}')
    if char_class == 'mage':
        ataka_m: int = 5 + randint(5, 10)
        return (f'{char_name} нанёс урон противнику равный {ataka_m}')
    if char_class == 'healer':
        ataka_h: int = 5 + randint(-3, -1)
        return (f'{char_name} нанёс урон противнику равный {ataka_h}')
    return f'{char_name} нанёс урон равный {5}'


def defence(char_name: str,
            char_class: str) -> str:
    """Вычисляет количество блокированного урона."""
    if char_class == 'warrior':
        return (f'{char_name} блокировал {10 + randint(5, 10)} урона')
    if char_class == 'mage':
        return (f'{char_name} блокировал {10 + randint(-2, 2)} урона')
    if char_class == 'healer':
        return (f'{char_name} блокировал {10 + randint(2, 5)} урона')
    return (f'{char_name} блокировал {10} урона')


def special(char_name: str,
            char_class: str) -> str:
    """Возвращает примененную спец-способность."""
    if char_class == 'warrior':
        special_w = (f'«Выносливость {80 + 25}»')
        return (f'{char_name} применил специальное умение {special_w}')
    if char_class == 'mage':
        special_m = (f'«Атака {5 + 40}»')
        return (f'{char_name} применил специальное умение {special_m}')
    if char_class == 'healer':
        special_h = (f'«Защита {10 + 30}»')
        return (f'{char_name} применил специальное умение {special_h}')
    return (f'{char_name} не применил специального умения')


def start_training(char_name: str,
                   char_class: str) -> str:
    """Определяет вводимую игроком команду.

    Возвращает результат выбранной команды.
    """
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: '
          'attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника или '
          'special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd: str = ''
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class() -> str:
    """Позволяет выбрать класс персонажа."""
    approve_choice: str = ''
    char_class: str = ''
    while approve_choice != 'y':
        char_class = input(
            'Введи название персонажа, '
            'за которого хочешь играть: '
            'Воитель — warrior, '
            'Маг — mage, '
            'Лекарь — healer: ',
        )
        if char_class == 'warrior':
            print('Воитель — дерзкий воин ближнего боя. '
                  'Сильный, выносливый и отважный.')
        if char_class == 'mage':
            print('Маг — находчивый воин дальнего боя. '
                  'Обладает высоким интеллектом.')
        if char_class == 'healer':
            print('Лекарь — могущественный заклинатель. '
                  'Черпает силы из природы, веры и духов.')
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, '
                               'или любую другую кнопку, '
                               'чтобы выбрать другого персонажа ').lower()
    return char_class


if __name__ == '__main__':
    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class = choice_char_class()
    print(start_training(char_name, char_class))
