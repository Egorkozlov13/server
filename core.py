from datetime import datetime

def handle_command(command):
    parts = command.split()
    
    if not parts:
        return "Ошибка: команда не распознана."

    cmd = parts[0].lower()

    if cmd == "поздоровайся" and len(parts) > 2:
        name = ' '.join(parts[2:])  # Имя может состоять из нескольких слов
        return f"Привет, {name}!"

    elif cmd == "какое" and len(parts) > 1 and parts[1].lower() == "сегодня" and len(parts) == 3 and parts[2].lower() == "число":
        return f"Сегодня {datetime.now().day}."

    elif cmd == "какая" and len(parts) > 1 and parts[1].lower() == "сегодня" and len(parts) == 3 and parts[2].lower() == "дата":
        return f"Сегодня {datetime.now().strftime('%d.%m.%Y')}."

    elif cmd == "сложи":
        try:
            numbers = list(map(int, parts[1:]))
            return str(sum(numbers))
        except ValueError:
            return "Ошибка: все аргументы должны быть числами."

    elif cmd == "вычти":
        try:
            if len(parts) != 3:
                return "Ошибка: команда должна содержать два числа."
            num1, num2 = map(int, parts[1:])
            return str(num1 - num2)
        except ValueError:
            return "Ошибка: все аргументы должны быть числами."

    elif cmd == "умножь":
        try:
            numbers = list(map(int, parts[1:]))
            result = 1
            for number in numbers:
                result *= number
            return str(result)
        except ValueError:
            return "Ошибка: все аргументы должны быть числами."

    elif cmd == "подели":
        try:
            if len(parts) != 3:
                return "Ошибка: команда должна содержать два числа."
            num1, num2 = map(int, parts[1:])
            if num2 == 0:
                return "Ошибка: деление на ноль."
            return str(num1 / num2)
        except ValueError:
            return "Ошибка: все аргументы должны быть числами."

    else:
        return "Ошибка: команда не распознана."