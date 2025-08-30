class Smartphone:
    def __init__(self, brand, model, storage, color):
        self.brand = brand  # The brand of the smartphone
        self.model = model  # The model name or number
        self.storage = storage  # The storage capacity (in GB)
        self.color = color  # The color of the phone
    
    def make_call(self, phone_number):
        print(f"Calling {phone_number}...")
    
    def send_text(self, phone_number, message):
        print(f"Sending text to {phone_number}: {message}")
    
    def take_picture(self):
        print(f"Taking a picture with the {self.model}'s camera!")
    
    def display_info(self):
        print(f"Smartphone Details: {self.brand} {self.model}, {self.storage}GB, Color: {self.color}")

# Create an instance of the Smartphone class
my_phone = Smartphone("Apple", "iPhone 14", 128, "Midnight")
my_phone.display_info()
my_phone.make_call("123-456-7890")
my_phone.take_picture()

class Vehicle:
    def move(self):
        pass  # This is a base class, so we don't define move() here.

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# Test Polymorphism
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    vehicle.move()
