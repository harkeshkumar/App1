import random

class Utility():
    
    def getRandomNumber():
        """
           Returns the Random number between 1000 to 5000
        """
        return random.randint(1000,5000)
    
    def getReverseString(str):
        """Parameter: String
           Returns the Reversed string
        """
        return str[::-1]