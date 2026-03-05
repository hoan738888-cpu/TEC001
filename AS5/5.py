import random


def estimate_pi(num_points: int) -> float:
    points_inside_circle = 0

    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x ** 2 + y ** 2 < 1:
            points_inside_circle += 1

    return 4 * points_inside_circle / num_points


def main():
    num_points = int(input("How many random points to generate? "))
    pi_approximation = estimate_pi(num_points)
    print(f"Approximation of π with {num_points:,} points: {pi_approximation}")
    print(f"Actual π:                                      3.141592653589793")
    print(f"Difference:                                    {abs(pi_approximation - 3.141592653589793):.10f}")


main()