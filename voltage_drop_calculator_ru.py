# ============================================
# Калькулятор падения напряжения для электриков
# Автор: Mohamed
# Описание: Расчёт падения напряжения в кабелях
# ============================================

def get_inputs():
    voltage = float(input("Введите напряжение сети (220 или 380): "))
    current = float(input("Введите ток (Амперы): "))
    length = float(input("Введите длину кабеля (метры): "))
    area = float(input("Введите сечение кабеля (мм²): "))
    material = input("Тип кабеля (copper / aluminum): ").lower()

    return voltage, current, length, area, material


def calculate_voltage_drop(voltage, current, length, area, material):
    if material == "copper":
        resistivity = 0.0175
    else:
        resistivity = 0.0282

    resistance = (resistivity * length) / area
    drop = current * resistance

    percent = (drop / voltage) * 100
    return drop, percent


def safety_check(percent):
    if percent <= 3:
        return "Система отличная и безопасная "
    elif percent <= 5:
        return "Допустимо, но близко к пределу "
    else:
        return "Опасно! Нужно увеличить сечение кабеля "


def main():
    print("\n===================================")
    print("   КАЛЬКУЛЯТОР ПАДЕНИЯ НАПРЯЖЕНИЯ")
    print("===================================\n")

    voltage, current, length, area, material = get_inputs()
    drop, percent = calculate_voltage_drop(voltage, current, length, area, material)
    status = safety_check(percent)

    print("\n========== ОТЧЁТ ==========")
    print(f"Падение напряжения: {drop:.2f} Вольт")
    print(f"Процент падения: {percent:.2f} %")
    print(f"Статус: {status}")
    print("============================\n")


main()
