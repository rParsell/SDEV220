class Vehicle:
    def __init__(self,type):
        self.type = type
class Automobile(Vehicle,):
    def __init__(self,year, make, model, doors, roof):
        self.year=year
        self.make=make
        self.model=model
        self.doors=doors
        self.roof=roof
storeDoors = ''
storeMake = ''
storeModel = ''
storeRoof = ''
storeYear = ''


print('What is the year of the car?')
storeYear=input()
print('What is the make of the car?')
storeMake=input()
print('What is the model of the car?')
storeModel=input()
print('How many doors does the car have?(2 or 4)')
storeDoors=input()
print('Does the car have a sun roof or solid roof(solid or sun roof)')
storeRoof=input()

v1 = Automobile(storeYear,storeMake,storeModel,storeDoors,storeRoof)
v1.type = 'car'
print('Vehicle Type: ' + v1.type)
print('Year: ' + v1.year)
print('Make: ' + v1.make)
print('Model: ' + v1.model)
print('Doors: ' + v1.doors)
print('Roof: ' + v1.roof)