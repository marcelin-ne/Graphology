"""This class is the profile of the person made by a questionary and info astrology"""
import Astrology
from Questionary import Questionary

class Profile:
    #objects
    char = None
    hobb = None
    questionary = Questionary()
    date = "01/01/2000"



    def setTemperament(self):
        self.chr = Questionary.ask_characteristics()

    def setHobbies(self):
        self.hobb = Questionary.ask_hobbies()
    
    def setAstrology(self,date):
        self.astrology = Astrology.setAstrology(date)

    def printProfile(self):
        print("Características de la Persona :  \n ")
        print(self.chr)
        print("Hobbies de la Persona :  \n ")
        print(self.hobb)
        print("Astrologia de la Persona :  \n ")

def main():
        profile = Profile()
        date=input("Ingrese su fecha de nacimiento en formato mm/dd/yyyy: \n  ")
        profile.setTemperament()
        profile.setHobbies()
        profile.printProfile()
        profile.setAstrology(date)
        
main()
