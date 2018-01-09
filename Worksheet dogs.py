class Dog:
    name
    colour

    def new(self, myName, myColour):
    name = myName
    colour = myColour

    def bark(barkTimes):
        for n = 1 to barktimes
            print(“Woof!”)

    def setcolour(self, dogcolour):
        Colour = dogcolour

    def getcolour():
        return colour

    def getname():
        return name

class Puppy(Dog):

    shoesChewed = 0

    def new(self, myName, myColour, myDob):
        Dog.new(myName, myColour)
        dob = myDob

    def chewShoe(self, numShoes):
        shoesChewed = shoesChewed + numShoes


    def getShoesChewed():
        return shoesChewed


myPuppy1 = Puppy(“Destoyer of Worlds”, “Jet Black”)
myPuppy1.chewShoe(5)
print(getname + “, “ + getShoesChewed)


myDog3 = Dog(“Mutt”, “Unknown”)
myDog4 = Dog(“Jeff”, “Unkown”)
