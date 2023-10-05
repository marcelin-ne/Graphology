#this class takes 2 dates and build a  astrological compatibility report

import Astrology
class CompatibilityByAstrology:
    #objects
    firstAstrologyprofile = ""
    secondAstrologyprofile = "" 
    #constructor
    def __init__(self, date1, date2):
        self.firstAstrologyprofile = Astrology.Astrology(date1)
        self.secondAstrologyprofile = Astrology.Astrology(date2)
    #methods
    #Get the first compatible element, if the first compatible element of the first person is the same as the element of the second person, then the first person is compatible with the second person in a 100%? if not then verify the second compatible element of the first person and compare it with the element of the second person, if they are the same then the first person is compatible with the second person in a 50%? if not then the first person is not compatible with the second person in a 0%?
    def getFirstCompatible(self):
        if self.firstAstrologyprofile.fcompatible == self.secondAstrologyprofile.element:
            return 100
        elif  self.firstAstrologyprofile.scompatible == self.secondAstrologyprofile.element:
            return 50
        else:
            return 0
        
def main():
    date1= "05/25/1999"
    date2= "04/18/2002"
    compatibility= CompatibilityByAstrology(date1, date2)
    print("first person's sign is: " + compatibility.firstAstrologyprofile.sign)
    print("second person's sign is: " + compatibility.secondAstrologyprofile.sign) 
    print ("first person's element is: " + compatibility.firstAstrologyprofile.element)
    print ("second person's element is: " + compatibility.secondAstrologyprofile.element)
    print("They are compatible in a " + str(compatibility.getFirstCompatible()) + "%")


main()

