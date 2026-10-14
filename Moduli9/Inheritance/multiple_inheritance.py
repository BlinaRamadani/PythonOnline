class Vertebrate:
    def __init__(self, backbone = True):
        self.has_backbone = backbone
    def vertebrate_info(self):
        print("Vertebrates have a backbone")

class Aquatic:
    def __init__(self, habitat="water"):
        self.habitat = habitat
    def aquatic_info(self):
        print("Aquatics animals live in water.")

class Fish (Vertebrate, Aquatic):
    def __init__(self, spicies, backbone=True, habitat="water"):
        self.habitat = habitat
        self.spicies = spicies

    def fish_info(self):
        print(f"The {self.spicies} is a type of fish found in {self.habitat}.")
    def swim(self):
        print("The fish is swimming")

goldfish = Fish("Goldfish")
print(goldfish.has_backbone)
print(goldfish.habitat)
goldfish.aquatic_info()
goldfish.vertebrate_info()
goldfish.fish_info()
goldfish.swim()