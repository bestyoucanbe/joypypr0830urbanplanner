# In this exercise, you are going to define your own Building type and create several instances of it to design your own virtual city. Create a class named Building in the building.py file and define the following fields, properties, and methods.

# Properties
# designer - It will hold your name.
# date_constructed - This will hold the exact time the building was created.
# owner - This will store the same of the person who owns the building.
# address
# stories
import datetime


class Building:

    def __init__(self, address, stories):
        self.designer = ""
        self.date_constructed = ""
        self.owner = ""
        self.address = address
        self.stories = stories

# Methods
# Define a construct() method. The method's logic should set the date_constructed field's value to datetime.datetime.now(). You will need to have import datetime at the top of your file.

# Define a purchase() method. The method should accept a single string argument of the name of the person purchasing a building. The method should take that string and assign it to the owner property.

    def construct(self):
        self.date_constructed = datetime.datetime.now().strftime("%x")

    def purchase(self, personbuying):
        self.owner = personbuying

# Constructor
# Define your __init__ method to accept two arguments

# address
# stories

# -->Modified self_init on Building

# Create 5 building instances


FirstBuilding = Building("101 1st Street", 10)
SecondBuilding = Building("202 2nd Street", 20)
ThirdBuilding = Building("303 3rd Street", 30)
FourthBuilding = Building("404 4th Street", 40)
FifthBuilding = Building("505 5th Street", 50)

# Have each one get purchased by a real estate magnate

FirstBuilding.purchase("RealEstateMagnate1")
SecondBuilding.purchase("RealEstateMagnate2")
ThirdBuilding.purchase("RealEstateMagnate3")
FourthBuilding.purchase("RealEstateMagnate4")
FifthBuilding.purchase("RealEstateMagnate5")

# After purchased, construct each one

FirstBuilding.construct()
SecondBuilding.construct()
ThirdBuilding.construct()
FourthBuilding.construct()
FifthBuilding.construct()

# Once all building are purchased and constructed, print the address, owner, stories, and date constructed to the terminal for each one.
# Example
# 800 8th Street was purchased by Bob Builder on 03/14/2018 and has 12 stories.

print(f'{FirstBuilding.address} was purchased by {FirstBuilding.owner} on {FirstBuilding.date_constructed} and has {FirstBuilding.stories} stories')
print(f'{SecondBuilding.address} was purchased by {SecondBuilding.owner} on {SecondBuilding.date_constructed} and has {SecondBuilding.stories} stories')
print(f'{ThirdBuilding.address} was purchased by {ThirdBuilding.owner} on {ThirdBuilding.date_constructed} and has {ThirdBuilding.stories} stories')
print(f'{FourthBuilding.address} was purchased by {FourthBuilding.owner} on {FourthBuilding.date_constructed} and has {FourthBuilding.stories} stories')
print(f'{FifthBuilding.address} was purchased by {FifthBuilding.owner} on {FifthBuilding.date_constructed} and has {FifthBuilding.stories} stories')
