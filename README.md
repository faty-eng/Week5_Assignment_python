# 📱🚗 OOP Demo: Smartphone & Vehicle Simulator

This project demonstrates fundamental Object-Oriented Programming (OOP) concepts in Python using two real-world domains:

A Smartphone class to simulate phone behaviors

A Vehicle class hierarchy to demonstrate polymorphism

## 📂 Project Structure
project/
│
├── smartphone_vehicle_demo.py   # Main Python script
└── README.md                    # Project documentation

## 🧠 Concepts Covered

Encapsulation: Grouping data and methods within classes (Smartphone)

Inheritance: Creating subclasses from a base class (Vehicle, Car, Plane, Boat)

Polymorphism: Using the same interface (move) to perform different behaviors

## 🚀 How to Run

Make sure you have Python installed (python3).

Clone or download this repository.

Run the script:

python smartphone_vehicle_demo.py

## 📱 Smartphone Class

Simulates a smartphone with:

make_call(phone_number)

send_text(phone_number, message)

take_picture()

display_info()

## Example:
my_phone = Smartphone("Apple", "iPhone 14", 128, "Midnight")
my_phone.display_info()
my_phone.make_call("123-456-7890")
my_phone.take_picture()

# 🚗 Vehicle Class Hierarchy

Demonstrates polymorphism using a common move() method.

## Classes:

Vehicle (base class)

Car → move() prints "Driving 🚗"

Plane → move() prints "Flying ✈️"

Boat → move() prints "Sailing 🚤"

## Example:
vehicles = [Car(), Plane(), Boat()]
for vehicle in vehicles:
    vehicle.move()

## 🛠️ Possible Extensions

Add a __str__() method for better object representation

Make Vehicle an abstract base class using abc.ABC

Expand the Smartphone class with battery life, camera resolution, etc.

Create a menu-driven interface for user interaction

## 📄 License

This project is open-source and free to use for educational purposes
