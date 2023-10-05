#this program tells you your zodiacal sign, element and compatible element from your date of birth
class Astrology:
    date = ""
    sign = ""
    element = ""
    fcompatible = ""
    scompatible = ""
    
    def __init__(self, date):
        self.date = date
        self.sign = self.getSign()
        self.element = self.getElement()
        self.fcompatible = self.getFirstCompatible()
        self.scompatible = self.getSecondCompatible()
    
    #* This class tells wich one is you first comapatible element 
    def getFirstCompatible(self):
        if self.element == "Fire":
            return "Fire"
        elif self.element == "Air":
            return "Air"
        elif self.element == "Water":
            return "Water"
        elif self.element == "Earth":
            return "Earth"
    
    #* This class tells wich one is you second  comapatible element 
    def getSecondCompatible(self):
        if self.element == "Fire":
            return "Air"
        elif self.element == "Air":
            return "Fire"
        elif self.element == "Water":
            return "Earth"
        elif self.element == "Earth":
            return "Water"
        
    #* This class tells wich one is your element from your zodiacal sign
    def getElement(self):
        if self.sign == "Aries" or self.sign == "Leo" or self.sign == "Sagittarius":
            return "Fire"
        elif self.sign == "Taurus" or self.sign == "Virgo" or self.sign == "Capricorn":
            return "Earth"
        elif self.sign == "Gemini" or self.sign == "Libra" or self.sign == "Aquarius":
            return "Air"
        elif self.sign == "Cancer" or self.sign == "Scorpio" or self.sign == "Pisces":
            return "Water"
        
    #* This class tells wich one is your zodiacal sign from your date of birth
    def getSign(self):
        month = int(self.date[0:2])
        day = int(self.date[3:5])
        if month == 1:
            if day < 20:
                return "Capricorn"
            else:
                return "Aquarius"
        elif month == 2:
            if day < 19:
                return "Aquarius"
            else:
                return "Pisces"
        elif month == 3:
            if day < 21:
                return "Pisces"
            else:
                return "Aries"
        elif month == 4:
            if day < 20:
                return "Aries"
            else:
                return "Taurus"
        elif month == 5:
            if day < 21:
                return "Taurus"
            else:
                return "Gemini"
        elif month == 6:
            if day < 21:
                return "Gemini"
            else:
                return "Cancer"
        elif month == 7:
            if day < 23:
                return "Cancer"
            else:
                return "Leo"
        elif month == 8:
            if day < 23:
                return "Leo"
            else:
                return "Virgo"
        elif month == 9:
            if day < 23:
                return "Virgo"
            else:
                return "Libra"
        elif month == 10:
            if day < 23:
                return "Libra"
            else:
                return "Scorpio"
        elif month == 11:
            if day < 22:
                return "Scorpio"
            else:
                return "Sagittarius"
        elif month == 12:
            if day < 22:
                return "Sagittarius"
            else:
                return "Capricorn"
            
    #* This class prints your zodiacal sign, element and compatible element with a date input by the user
    def print(self):
        print("Your zodiacal sign is: " + self.sign)
        print("Your element is: " + self.element)
        print("Your first  compatible element is: " + self.fcompatible)
        print("Your second compatible element is: " + self.scompatible)  

#* This function asks the user for a date and returns it
def askDate():
    date = input("Enter your date of birth (MM/DD): ")
    return date

#* Main function
def main():
    date = askDate()
    astrology = Astrology(date) #* Create an object of the class Astrology
    astrology.print() #* Print the zodiacal sign, element and compatible element 


main() #* Call the main function