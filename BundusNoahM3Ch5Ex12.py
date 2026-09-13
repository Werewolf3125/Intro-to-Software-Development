def falling_distance(time_falling: float) -> float:
    # Using the formula: d = 0.5 * g * t^2, where g = 9.8 m/s^2
    gravity = 9.8
    fall_distance = 0.5 * gravity * time_falling ** 2
    return fall_distance

def results(time_falling: float, fall_distance: float) -> None:
    print(f"Time Falling: {time_falling:.2f} seconds")
    print(f"Fall Distance: {fall_distance:.2f} meters")

def main() -> None:
    time_falling = 1
    for _ in range(10):
        fall_distance = falling_distance(time_falling)
        results(time_falling, fall_distance)
        time_falling += 1

main()