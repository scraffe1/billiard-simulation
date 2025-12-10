import numpy as np
import matplotlib.pyplot as plt
import math


# ------------------------------
# ПАРАМЕТРЫ СТОЛА
# ------------------------------
TABLE_WIDTH = 2.0   # метров
TABLE_HEIGHT = 1.0  # метров


def simulate_trajectory(speed_m_s: float,
                        angle_deg: float,
                        total_time: float = 10.0,
                        dt: float = 0.01):
    """
    Расчёт траектории шарика на прямоугольном столе.

    speed_m_s  - скорость в м/с
    angle_deg  - угол в градусах (0° вправо, 90° вверх)
    total_time - общее время моделирования в секундах
    dt         - шаг по времени
    """
    angle_rad = math.radians(angle_deg)

    # раскладываем скорость на компоненты
    vx = speed_m_s * math.cos(angle_rad)
    vy = speed_m_s * math.sin(angle_rad)

    # начальное положение — центр стола
    x = TABLE_WIDTH / 2.0
    y = TABLE_HEIGHT / 2.0

    positions = []

    t = 0.0
    while t <= total_time:
        positions.append((x, y))

        x += vx * dt
        y += vy * dt

        # отражение от стен
        if x <= 0.0:
            x = -x
            vx = -vx
        elif x >= TABLE_WIDTH:
            x = 2 * TABLE_WIDTH - x
            vx = -vx

        if y <= 0.0:
            y = -y
            vy = -vy
        elif y >= TABLE_HEIGHT:
            y = 2 * TABLE_HEIGHT - y
            vy = -vy

        t += dt

    return np.array(positions)


def main():
    print("МОДЕЛИРОВАНИЕ ДВИЖЕНИЯ ШАРИКА НА СТОЛЕ")
    print("--------------------------------------")

    speed_str = input("Введите скорость (м/с): ").strip()
    angle_str = input("Введите угол (градусы): ").strip()

    try:
        speed = float(speed_str.replace(",", "."))
        angle = float(angle_str.replace(",", "."))
    except ValueError:
        print("Ошибка: введите числа.")
        return

    if speed <= 0:
        print("Скорость должна быть положительной.")
        return

    positions = simulate_trajectory(speed, angle)

    fig, ax = plt.subplots(figsize=(8, 4))

    ax.plot([0, TABLE_WIDTH, TABLE_WIDTH, 0, 0],
            [0, 0, TABLE_HEIGHT, TABLE_HEIGHT, 0],
            'k-', linewidth=2)

    ax.plot(positions[:, 0], positions[:, 1], 'b-')
    ax.plot(positions[-1, 0], positions[-1, 1], 'ro')

    ax.set_aspect('equal')
    ax.set_xlabel("x, м")
    ax.set_ylabel("y, м")
    ax.set_title("Траектория движения шарика")

    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
