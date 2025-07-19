# Everything in Python is an object, including functions and classes.
# class has two things in it:-
# 1. funtion = behaviour
# 2. data = properties/ attributes
# Class is a blueprint for creating objects (instances).
# there are two types of classes:
# 1. User defined class 
# 2. Built-in class
class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
    
# Creating an instance of the student class
# s1 = student("Alice", 20)
# Calling the display method to show the student's information
# s1.display()
# Output: Name: Alice, Age: 20
# The above code defines a class 'student' with an initializer and a method to display student information.
# The class is then instantiated, and the method is called to demonstrate its functionality.

# Writing Code for an ATM machine

class ATM:
    def __init__(self):
        self.pin=''
        self.balance=0
        self.inputPin=''
        self.menu() # calling menu() from const

    def validatePin(self):
        if self.pin=='':
            print('You have not created a pin.\nPlease create a 4 digit pin.')
            self.setPin()
        pin=input("Enter the pin: ")
        if self.pin!=pin:
            return False
        else:
            return True

    def checkBalace(self):
        return f'Balance: {self.balance}'
    
    def setPin(self):
        if self.pin=='':
            pin=input('Enter new pin:')
            self.pin=pin
        else:
            reuslt=self.validatePin()
            if reuslt:
                pin=input('Enter new pin:')
                self.pin=pin
            else:
                print('You have entered the wrong pin.')
                
                

    def deposit(self,amount):
            self.balance+=amount
            print( f"Balance: {self.balance}")
    
    def withdraw(self,amount):
        if self.balance < amount:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrawal successful. Remaining balance: {self.balance}")
    
    def menu(self):
        flag=True
        while flag:
            option=input("""Choose an Option:
                     1. set pin.
                     2. check balance.
                     3. deposit money.
                     4. withdraw money.
                     5. Exit.""")
            if option=='1':
                self.setPin()
            elif option == '2':
                print(self.checkBalace())
            elif option == '3':
                isCorrect=self.validatePin()
                if isCorrect:
                    amount=int(input('Enter the amount to be deposited: '))
                    self.deposit(amount)
                else:
                    print(f"You have entered the wrong pin.\nPlease enter the correct pin.")
            elif option == '4':
                isCorrect=self.validatePin()
                if isCorrect:
                    amount=int(input('Enter the amount to be withdrawn: '))
                    self.withdraw(amount)
                else:
                    print(f"You have entered the wrong pin.\nPlease enter the correct pin.")
            else:
                flag=False

newUser=ATM()
newUser


# methods vs funtions
# function inside a class is called method and outside it is called function.
# class diagram:- class can be represented using a diagram
################################
#         ATM                  #
################################
#       +  Data                #
#       -                      #
################################ 
#                              #
#                              #                     
#                              #
#                              #
#                              #
#     +      mehtods           #
#     -                        #
#                              #
#                              #
#                              #
#                              #
#      +=>Public               #
#      -=>private              #
#                              #
################################


# Magic methods
# A magic method is a special kind of method syntax= __nameOfMethod__()
# they have some special functionality

# example: __init__()

# constructor is a magicMethod, it doesn't need to be called it gets triggered automatically 
# as sson as the object of the class
# is created.
# contructor helps to initialise the data and methods.
#  There are more than 150 magic Methods
# you cannot change the name of the constructor.

# self is a reference to the current instance of the class.
# It is used to access variables that belong to the class.
# It does not have to be named self, but it is a strong convention to use this name.
# self is used to access the attributes and methods of the class in Python.
# It binds the attributes with the given arguments.
# self is the first parameter of the method, it refers to the instance of the class.
# It is used to access variables that belong to the class.
# self is used to differentiate between instance variables and local variables.
# It is used to access the attributes and methods of the class in Python.