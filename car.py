# I took this example from pynative.com to practise/learn 
# Object Oriented Programming. 
#
# SUCCESS! This was the first time that I created a class
# and got the code to run. It ran within an online code 
# editor from pynative.com.

# It also runs within python3 version 3.8.2 pn my Macbook
# within VS Code


class Car:
    '''
       This is my example car class.

       This is the constructor for the 
       object class Car. The __init__() 
       method initializes the object
    
    '''
    def __init__(self, make, model, year, tires):
        # data members (instance variables)
        self.make = make
        self.model = model
        self.year = year
        self.tires = tires
        
    # Behavior (instance methods)
    # one way to print information anout a car instance
    def show(self):
        print('Make:', self.make, 'Model:', self.model, 'Year:', self.year,'\n')
    
    # Behavior (instance methods)
    # Another way to print info about a car instance
    def theMod(self):
        print('The car is a', self.year, ' ' , self.make, ' Model ', self.model,'\n')  

    # Behavior (instance method)
    # Show the tire info about the car instance
    def theTires(self):
        print('The tires on ',self.make,' are: ', self.tires,' brand. \n')

    # class method
    @classmethod
    def modify_tires(cls, new_tires):
        # modify class tires as you might buy new tires but
        # make, model and year will not change
        cls.car_tires = new_tires
        
# Create an object for Michiko from class Car
michiko = Car('Subaru','Outback','2015','Falken')

# Example of using getattr() instead of self.make
print('**********\n')
print('Make:', getattr(michiko,'make'))
print('\n')

# Call the 2 methods
michiko.show()
michiko.theMod()
michiko.theTires()

# Now the Highlander
toy_highland = Car('Toyota','Highlander','2022','Michelin')

# Call some methods
toy_highland.show()
toy_highland.theMod()
toy_highland.theTires()

# Change the tires on the Toyota
toy_highland.modify_tires('Yokohama')
# Show the tires and see if the tires were indeed changed.
toy_highland.theTires()



