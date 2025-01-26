import datetime

def handle_command(command):
    if command.startswith("Поздоровайся с"):
        name = command.split("с")[-1].strip()
        return f"Привет, {name}!"
    elif command == "Какое сегодня число":
        return datetime.datetime.now().strftime("%Y-%m-%d")
    elif command.startswith("Сложи"):
        numbers = list(map(float, command.split()[1:]))
        return str(sum(numbers))
    elif command.startswith("Вычти"):
        numbers = list(map(float, command.split()[1:]))
        if len(numbers) == 2:
            return str(numbers[0] - numbers[1])
        else:
            return "Пожалуйста, укажите два числа для вычитания."
    elif command.startswith("Умножь"):
        numbers = list(map(float, command.split()[1:]))
        result = 1
        for number in numbers:
            result *= number
        return str(result)
    elif command.startswith("Раздели"):
        numbers = list(map(float, command.split()[1:]))
        if len(numbers) == 2:
            if numbers[1] != 0:
                return str(numbers[0] / numbers[1])
            else:
                return "Ошибка: деление на ноль."
        else:
            return "Пожалуйста, укажите два числа для деления."
    else:
        return "Неизвестная команда."