import math
def calculate_pizza_unit_price(diameter_cm, price_usd):
    radius_m = (diameter_cm / 2) / 100  # Convert to meters
    area_m2 = math.pi * (radius_m ** 2)
    unit_price = price_usd / area_m2
    return unit_price
if __name__ == "__main__":
    # Get first pizza information
    print("Enter details for Pizza 1:")
    diameter1 = float(input("Enter the diameter in centimeters: "))
    price1 = float(input("Enter the price in USD: "))
    print("\nEnter details for Pizza 2:")
    diameter2 = float(input("Enter the diameter in centimeters: "))
    price2 = float(input("Enter the price in USD: "))
    unit_price1 = calculate_pizza_unit_price(diameter1, price1)
    unit_price2 = calculate_pizza_unit_price(diameter2, price2)
    print(f"\nPizza 1 unit price: ${unit_price1:.2f} per square meter")
    print(f"Pizza 2 unit price: ${unit_price2:.2f} per square meter")
    if unit_price1 < unit_price2:
        print("\nPizza 1 provides better value for money.")
    elif unit_price2 < unit_price1:
        print("\nPizza 2 provides better value for money.")
    else:
        print("\nBoth pizzas have the same value for money.")