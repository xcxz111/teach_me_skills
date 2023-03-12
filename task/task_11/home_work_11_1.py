# Создать генератор геометрической прогрессии
# Подключить дебаггинг
# Сделать функцию для фильтрации email


def geometric_progression(start, factor):
    current = start
    while True:
        yield current
        current *= factor




