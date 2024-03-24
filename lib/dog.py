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
            # print(f"Setting name to { name}.")
            # print statements need to be commented out to pass tests
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")


    def get_breed(self):
        print("Retrieving breed.")
        return self._breed
    
    def set_breed(self, breed): 
        if breed in APPROVED_BREEDS:
            # print(f"Setting breed to {breed}.")
            # print statements need to be commented out to pass tests
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")

    name = property(get_name, set_name)
    breed = property(get_breed, set_breed)
