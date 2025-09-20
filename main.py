# ************************************************************ HEADER ************************************************************ #
# - Assignment 1: Hello World
#
# - Name: Faheem Saeed
# - Student ID: 18133158
# - File: main.py
# - Purpose: Contains the main function, which serves to display a hello world on a terminal.
# - Description: Main program source code, which uses a class called hello_world. The class hello_world has 2 functions.
# The first function __init__(self, statement) initializes an object which has a label called statement in it. It also sets the input statement
# to the object. The second function called greet(self) utilizes the created object to print the label statement in it. 
# To compile this code, utilize pyinstaller as indicated in the README.md. To use this code for displaying another statement on the terminal, 
# alter the global variable <statement>.

# ************************************************************ REFERENCED MATERIAL *********************************************** #

#ChatGPT used for instructions on how to setup the class, and definitions related to __init__, {} usage, etc.
#as it has been some time since I have coded in python.
#I learnt how to use pyinstaller from ChatGPT to bundle the application and its dependencies into an exe file.
#Used ChatGPT for code review - to see if following PEP 8 coding stylization for Python, and determine differences to judge if acceptable or not.
#Referenced provided header example to setup header.

# ************************************************************ DEPENDENCIES ****************************************************** #

# Refer to requirements.txt for the list of libraries used and dependencies
import keyboard

# ************************************************************ GLOBAL VARIABLES ************************************************** #

# statement = "statement text here"

# ************************************************************ FUNCTION & CLASS DEFINITIONS ************************************** #

# Class: hello_world
# Arguments: (statement: str)
#       The string statement that you want to print onto the console - in this case hello world.
#       Constructor __init__ runs automatically when you create an object from the class.
#       It stores the statement inputted into a label called statement in the object using self.statement.

class hello_world:

    # Function: __init__
    # Arguments: self, statement
    # Returns: nothing
    # Logic: creates constructor which runs when you make an object from the class
    # It sets data up in the object, putting the statement text inside the object for later use.

    def __init__(self, statement: str) -> None:
        #self refers to the object being created, which has a label called statement inside it
        self.statement = statement

    # Function: greet(self)
    # Arguments: self
    # Returns: printed statement
    # Logic: function inside the class which is meant to allow the object to do an action
    # when you call the greet function with the object, it will print out the statement

    def greet(self) -> None:
        print(f"{self.statement}")

#storing string hello world onto statement global variable
statement = "Hello World"

#Creating a new object using the class hello world with the statement hello world inputted
#Uses input instead to wait for user to press a button then exits.
statement_obj = hello_world(statement)
statement_obj.greet()

# #Waits for a key to be pressed before exiting application.
# print("Press any button to exit...")
# keyboard.read_event()

