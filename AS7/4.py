
import random

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

    def __str__(self):
        return f"{self.registration_number:<10} | {self.max_speed:<12} | {self.current_speed:<12} | {self.travelled_distance:<15}"

#1
car = Car("ABC-123", 142)
print("Initial car properties:")
registration = int(input(print(f"Registration: {car.registration_number}, Max Speed: {car.max_speed}, Current Speed: {car.current_speed}, Distance: {car.travelled_distance}  ")))

#2
car.accelerate(30)
car.accelerate(70)
car.accelerate(50)
print("\nAfter accelerations:")
print(f"Current Speed: {car.current_speed}")

car.accelerate(-200)  # Emergency brake
print("After emergency brake:")
print(f"Final Speed: {car.current_speed}")

#3
car.current_speed = 60
car.travelled_distance = 2000
car.drive(1.5)
print("\nAfter driving 1.5 hours at 60 km/h:")
print(f"Travelled Distance: {car.travelled_distance}")

#4
cars = []
for i in range(1, 11):
    reg_number = f"ABC-{i}"
    max_speed = random.randint(150, 200)
    cars.append(Car(reg_number, max_speed))

race_hours = 0
race_finished = False

while not race_finished:
    race_hours += 1
    for car in cars:
        car.accelerate(random.randint(-10, 15))
        car.drive(1)
        if car.travelled_distance >= 10000:
            race_finished = True

print(f"\nRace finished in {race_hours} hours!\n")
print(f"{'Reg Number':<10} | {'Max Speed':<12} | {'Current Speed':<12} | {'Distance':<15}")
print("-" * 60)
for car in cars:
    print(car)
