

import pandas as pd

# Inherit from panda's DataFrame
class MyDataFrame(pd.DataFrame):
    def num_cells(self):
        return self.shape[0] * self.shape[1]

class Complex:
   def __init__(self, realpart, imagpart):
       self.r = realpart
       self.i = imagpart
    
    def add(self, other_complex):
        self.r += other_complex.r
        self.i += other_complex.i
    
    # Representation method. What makes it print out pretty details
    # Without it, you get computer's representation
    def __repr__(self):
        return '({}, {})'.format(self.r, self.i)

class SocialMediaUser:
    def __init__(self, name):
        self.name = name
        self.upvotes = 0
    
    def receive_upvote(self):
        self.upvotes += 1
    
    def is_popular(self):
        return self.upvotes > 100
    

class Animal:
    """
    General representation of animals.
    """
    def __init__(self, name, weight, diet_type):
        self.name = str(name)
        self.weight = weight
        self.diet_type = diet_type
    
    def run(self):
        return 'Vroom!'

    def eat(self, food):
        return food + ' is delicious, yum!'

# Subclass of Animal
class Tiger(Animal):
    """
    Representation of tigers, a subclass of Animal
    """
    # No need to redefine methods – inheritance goes in one direction
    # Must override parent's init method to add num_stripes
    def __init__(self, name, weight, diet_type, num_stripes):
        #Inside a subclass, super is a reference to whatever class you're inheriting from
        super().__init__(name, weight, diet_type)
        self.num_stripes = num_stripes
    
    def say_great(self):
        return "It's GRREAT!"
    
    # Example of overriding method from parent/Super class
    def run(self):
        return 'Scamperwoosh'
