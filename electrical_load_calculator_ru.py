# ============================================
# Умный калькулятор электрической нагрузки
# Автор: Mohamed
# Язык: Python
# Описание: Программа для электриков
# ============================================

def get_devices():
    devices = []
    count = int(input("Введите количество приборов: "))

    for i in range(count):
        name = input(f"\nВведите название прибора {i+1}: ")
        power = float(input(f"Введите мощность прибора '{name}' в ваттах (Вт): "))
        devices.append((name, power))

    return devices


def calculate_total_power(devices):
    total_power = 0
    for device in devices:
        total_power += device[1]
    return total_power


def calculate_current(total_power, voltage):
    current = total_power / voltage
    return current


def recommend_breaker(current):
    breakers = [6, 10, 16, 20, 25, 32, 40, 50, 63]

    for b in breakers:
        if current <= b:
            return b

    return "Более 63А (промышленный автомат)"


def recommend_cable(current):
    if current <= 10:
        return "1.5 мм²"
    elif current <= 16:
        return "2.5 мм²"
    elif current <= 25:
        return "4 мм²"
    elif current <= 32:
        return "6 мм²"
    elif current <= 40:
        return "10 мм²"
    elif current <= 63:
        return "16 мм²"
    else:
        return "25 мм² и выше"


def check_safety(current, breaker):
    if isinstance(breaker, int):
        if current > breaker * 0.8:
            return "⚠ ВНИМАНИЕ: Возможна перегрузка!"
        else:
            return "✅ Нагрузка в безопасном диапазоне."
    else:
        return "⚠ Очень высокий ток!"


def main():
    print("\n======================================")
    print("  УМНЫЙ КАЛЬКУЛЯТОР ЭЛЕКТРОНАГРУЗКИ")
    print("======================================\n")

    voltage = float(input("Введите напряжение сети (220 или 110): "))

    devices = get_devices()

    total_power = calculate_total_power(devices)
    current = calculate_current(total_power, voltage)
    breaker = recommend_breaker(current)
    cable = recommend_cable(current)
    safety = check_safety(current, breaker)

    print("\n========== ОТЧЁТ ==========")
    print(f"Общая мощность: {total_power:.2f} Вт")
    print(f"Общий ток: {current:.2f} А")
    print(f"Рекомендуемый автомат: {breaker} А")
    print(f"Рекомендуемое сечение кабеля: {cable}")
    print(f"Статус безопасности: {safety}")
    print("===========================\n")


if __name__ == "__main__":
    main()
