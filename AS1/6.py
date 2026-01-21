talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))
lots_in_pound = 32
pounds_in_talent = 20
grams_in_lot = 13.3
total_lots = (talents * pounds_in_talent * lots_in_pound) + (pounds * lots_in_pound) + lots
total_grams = total_lots * grams_in_lot
kilograms = int(total_grams // 1000)
grams = total_grams % 1000
print("The weight in modern units:")
print(f"{kilograms} kilograms and {grams:.2f} grams.")
