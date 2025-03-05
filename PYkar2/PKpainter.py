import emsine as emsineFail
import teine as teineFail




def turn_right():
    for _ in range(3):
        right()

def fill_room():
    """Заполняет всю комнату змейкой (сначала по горизонтали, затем по вертикали)."""
    row = 0  # Отслеживаем, на какой строке робот
    steps_count = 0  # Счетчик шагов

    while True:
        # Двигаемся по горизонтали
        while not is_wall():
            if not is_painted():
                paint()
            step()
            steps_count += 1  # Увеличиваем счетчик шагов

            # Если сделали 9 шагов подряд, поворачиваем направо
            if steps_count == 10:
                turn_right()
                steps_count = 0  # Сбрасываем счетчик шагов

        if not is_painted():  # Закрашиваем последнюю клетку перед стеной
            paint()

        # Переход на следующую строку
        if row % 2 == 0:  # На чётных строках поворачиваем 1 раз направо
            right()
            if is_wall():
                break  # Если справа стена, значит, всё закрашено
            step()
            right()
        else:  # На нечётных строках поворачиваем 3 раза (чтобы развернуться)
            turn_right()
            if is_wall():
                break
            step()
            turn_right()

        row += 1  # Переход к следующей строке

    # После завершения горизонтального движения, начинаем заполнять по вертикали
    col = 0
    while True:
        while not is_wall():
            if not is_painted():
                paint()
            step()
            steps_count += 1  # Увеличиваем счетчик шагов

            # Если сделали 9 шагов подряд, поворачиваем направо
            if steps_count == 11:
                turn_right()
                steps_count = 0  # Сбрасываем счетчик шагов

        if not is_painted():
            paint()

        # Переход на следующую вертикальную строку
        if col % 2 == 0:  # Если колонка чётная, двигаемся вниз
            right()
            if is_wall():
                break
            step()
            right()
        else:  # Если колонка нечётная, поворачиваем 3 раза (разворачиваемся)
            turn_right()
            if is_wall():
                break
            step()
            turn_right()

        col += 1

def move_to_next_room():
    """Ищет проход в следующую комнату и переходит в неё."""
    while True:
        if is_wall():
            right()
        else:
            step()
        
        if not is_wall() and not is_painted():  # Нашли новую незакрашенную область
            break


# Основной цикл: закрашиваем комнату, затем переходим в следующую
while True:
    fill_room()  # Заполняем текущую комнату
    
    # Ищем следующую комнату
    move_to_next_room()
