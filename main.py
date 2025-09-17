# ************************************************************ HEADER ************************************************************ #
# - Assignment 1: Hello World
#
# - Name: Faheem Saeed
# - Student ID: 18133158
# - File: main.py
# - Purpose: Contains the main function
# - Description: Entry for the program, including the main function The main application class as well as display
# - and support class is included.

# ************************************************************ REFERENCED MATERIAL *********************************************** #

#ChatGPT used for instructions on how to setup the class, and definitions related to __init__, {} usage, etc.
#as it has been some time since I have coded in python.
#I used pyinstaller which bundles python and its dependencies into an exe file.
#used pyinstaller to set it up
#Referenced provided header example to setup header.

# ************************************************************ DEPENDENCIES ****************************************************** #

# Refer to requirements.txt for the list of libraries used and dependencies
import keyboard

# ************************************************************ GLOBAL VARIABLES ************************************************** #

# statement = "statement text here"

# ************************************************************ FUNCTION & CLASS DEFINITIONS ************************************** #

# Class: hello_world
# Arguments & Parameters: (statement : str)
#       The string statement that you want to print onto the console - in this case hello world.
#       Constructor __init__ runs automatically when you create an object from the class.
#       It stores the statement inputted into a label called statement in the object using self.statement.

class hello_world:

    # Function: __init__
    # Arguments: self, statement
    # Returns: nothing
    # Logic: creates constructor which runs when you make an object from the class
    # It sets data up in the object, putting the statement text inside the object for later use.

    def __init__(self, statement):
        #self refers to the object being created, which has a label called statement inside it
        self.statement = statement

    # Function: greet(self)
    # Arguments: self
    # Returns: printed statement
    # Logic: function inside the class which is meant to allow the object to do an action
    # when you call the greet function with the object, it will print out the statement

    def greet(self):
        print(f"{self.statement}")

#storing string hello world onto statement global variable
statement = "Hello World"

#Creating a new object using the class hello world with the statement hello world inputted
#Uses input instead to wait for user to press a button then exits.
object = hello_world(statement)
object.greet()

#Waits for a key to be pressed before exiting application.
print("Press any button to exit...")
keyboard.read_event()

