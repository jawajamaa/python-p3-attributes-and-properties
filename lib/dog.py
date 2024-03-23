#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    species = "canine"

    def __init__(self, breed = "Mastiff", name = "Bounce"):
        self.name = name
        self.breed = breed

    def get_name(self):
        print("Retrieving name.")
        return self._name
    
    def set_name(self, name):
        if isinstance (name, str) and 1 <= len(name) <= 25:
        # if (type(name) is (str)) and (1 <= len(name) <= 25): less pythonic
            print(f"Setting name to { name}.")
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)

    def set_breed(self, breed): 
        pass   

fido = Dog("Fido")

# fido.showing_self()
