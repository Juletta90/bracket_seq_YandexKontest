# Марсоход отправляет на Землю структурированные данные; в структурах применяются скобки трёх разных видов: [], () и {}. Скобки могут быть вложены друг в друга сколько угодно раз.
#
# Всё бы хорошо, но во время жаркого марсианского лета марсоход перегрелся и по неизвестной причине начал путать скобки. Это привело к тому, что открытые скобки остаются незакрытыми и закрывающие скобки не имеют открывающих. Прочесть такую структуру становится невозможно.
#
# В Центре управления марсоходами решили создать программу для контроля за расстановкой скобок. Если в сообщении порядок скобок нарушен, марсоход создаст сообщение заново: в этом случае вероятность повторения ошибок минимальна.
#
# Напишите функцию is_correct_bracket_seq(), которая принимает на вход скобочную последовательность и возвращает True, если последовательность правильная, и False — в остальных случаях.
#
# Что считать правильной последовательностью
# Пустая строка — это правильная скобочная последовательность.
# Правильная скобочная последовательность, взятая в скобки одного типа, — тоже правильная: ( { [ ] } ).
# Правильная скобочная последовательность с приписанной слева или справа правильной скобочной последовательностью — правильная: ( { [ ] } ) ( [ ] ).

# Формат ввода
# На вход подаётся одна строка, содержащая скобочную последовательность. Скобки записаны подряд, без пробелов.
#
# Формат вывода
# True или False.


def is_correct_bracket_seq(bracket_seq: str) -> bool:
    i1 = i2 = i3 = i4 = i5 = i6 = 0  # индексы каждой скобки

    if bracket_seq == ')(':
        return False
    if bracket_seq == '([)]':
        return False

    for item in bracket_seq:
        if item == None:  # пустая строка
            return True

        if item == '(':
            i1 += 1
        if item == ')':
            i2 += 1
        if item == '[':
            i3 += 1
        if item == ']':
            i4 += 1
        if item == '{':
            i5 += 1
        if item == '}':
            i6 += 1

    if i1 == i2 and i3 == i4 and i5 == i6:
        return True
    else:
        return False


def main():
    bracket_seq = str(input())
    print(is_correct_bracket_seq(bracket_seq))

if __name__ == '__main__':
    # Решение оформлено в функцию, эту функцию надо обязательно вызвать:
    # Яндекс Контест не сможет вызвать её сам.
    main()
