class kActor:
    def __init__(self, name, age, drama):  # Encapsulation: Constructor to initialize object state
        self.name = name
        self.age = age
        self.drama = drama

    def introduce(self):  # Abstraction: Exposes only necessary features to interact with the class
        print(f"Name: {self.name}")
        print(f"Age: {self.age} years old")
        print(f"Drama: {self.drama}")

class kLeadActor(kActor):  # Inheritance: Build new classes on existing ones
    def __init__(self, name, age, drama, lead_role):  # Encapsulation: Inherits and extends encapsulated behavior
        super().__init__(name, age, drama)
        self.lead_role = lead_role

    def introduce(self):  # Polymorphism: Method overriding to customize behavior in subclasses
        super().introduce()
        print(f"Lead Role: {self.lead_role}")

# Create kActor objects
actor1 = kActor("Lee Jae-Wook", 25, "Alchemy of Souls")  # Classes and Objects: Creating an object of kActor
actor2 = kActor("Cha Eun-Woo", 27, "Wonderful World")    # Classes and Objects: Creating an object of kActor
actor3 = kActor("Byeon Woo-seok", 32, "Lovely Runner")   # Classes and Objects: Creating an object of kActor

# Create kLeadActor object
lead_actor1 = kLeadActor("Park Seo-Joon", 33, "Itaewon Class", "Park Sae-Ro-Yi")  # Classes and Objects: Creating an object of kLeadActor

# Access object attributes
print("==========================")
lead_actor1.introduce()
print("==========================")
actor1.introduce()
print("==========================")
actor2.introduce()
print("==========================")
actor3.introduce()
print("==========================")

