# ************************************************************ HEADER ************************************************************ #
# - Assignment 2: Area of Rectangle Calculator
#
# - Name: Faheem Saeed
# - Student ID: 18133158
# - File Name: main.py

# - Purpose: Contains the main method, which serves to calculate the area of the two rectangles given doubles for length and width information for
# the rectangles, then compares them to check if they are the same.

# - Description: Main program source code, which uses a class called rectangle_area_class. The class has 4 methods.
# The first method __init__(self, statement) initializes an object which has a attributes for the lengths and widths of the two rectangles. 
# The second method called eval_variables(self) utilizes the inputted attributes from the main function and checks if they are floats and positive non-zero
# numbers. It returns a list of booleans indicating if the parameters provided for both rectangles are correct for providing a positive real non-zero area.
# The third method area_calculator(self) calculates the areas of the two rectangles and puts them in a list, which is returned.
# The fourth method eval_area_similarity(self) compares the two areas in the list and verifies that they are equivalent to each other within a certain relative
# tolerance, provided to account for floating point base 2 errors in trying to quantify a base 10 decimal number.
# To compile this code, utilize pyinstaller as indicated in the README.md. To use this code for calculating the areas of other rectangles, alther the variables provided
# in the main function. To pack the script, follow the README.md instructions to use pyinstaller.

# ************************************************************ REFERENCED MATERIAL *********************************************** #

#ChatGPT used for reference on how to use typing notations to indicated expected variable type for classes in Python.
#ChatGPT used to understand how to utilize math.isclose to check if both areas similar within desired tolerance.
#ChatGPT used for code review - to see if following PEP 8 coding stylization for Python, and determine differences to judge if acceptable or not.
#Style followed is not exactly PEP-8, as Professor Christoph allows following own convention as long as consistency is shown.
#Referenced provided header example to setup header.

# ************************************************************ DEPENDENCIES ****************************************************** #
import sys
import math
# pyinstaller==6.0+ (below dependencies for pyinstaller)
# altgraph==0.17.4
# packaging==25.0
# pefile==2023.2.7
# pyinstaller==6.16.0
# pyinstaller-hooks-contrib==2025.9
# pywin32-ctypes==0.2.3
# setuptools==80.9.0

# ************************************************************ GLOBAL VARIABLES ************************************************** #

# No global variables present, all variables stored in main() function.

# ************************************************************ MAIN CLASS & METHOD DEFINITIONS ************************************** #

# Class: rectangle_area_class
# Arguments: (self, length1, length2, length3, length4)
#       The variables that you want to set to become the length and widths of the two triangles (double)
#       Constructor __init__ runs automatically when you create an object from the class.
#       It stores the variables inputted in the object using self.width1, self.width2, self.length1, self.length2

class rectangle_area_class:

    # Method: __init__
    # Arguments: self
    # Returns: nothing
    # Logic: creates constructor which runs when you make an object from the class
    # It sets data up in the object, putting the lengths and widths entered into attributes in the object for later use.

    def __init__(self, length1: float, length2: float, width1: float, width2: float) -> None:
        #self refers to the object being created, which initializes attributes called width1, width2, length1, length2 inside it and stores given values.
        self.length1 = length1
        self.length2 = length2
        self.width1 = width1
        self.width2 = width2

    # Method: eval_variables(self)
    # Arguments: self
    # Returns: variable_bool_list (list): a list of 4 booleans which evaluate to TRUE if the parameters provided are positive greater than zero floats
    # Logic: method inside the class which is meant to evaluate the attributes length1, length2, width1, width2 inside 
    # Evaluates each attribute to ensure that a float (C double) has been provided which is positive and greater than 0.

    def eval_variables(self) -> list[bool, bool, bool, bool]:
        
        length1_bool = isinstance(self.length1, float) and self.length1 > 0
        length2_bool = isinstance(self.length2, float) and self.length2 > 0
        width1_bool = isinstance(self.width1, float) and self.width1 > 0
        width2_bool = isinstance(self.width2, float) and self.width2 > 0

        variable_bool_list = [length1_bool, length2_bool, width1_bool, width2_bool]
        return variable_bool_list
    
    # Method: area_calculator(self)
    # Arguments: self
    # Returns: area_rect_list (list): a list of 2 floating point numbers which represent the areas of the two rectangles for the parameters provided.
    # Logic: method inside the class which is meant to calculate the area of two rectangles given the parameters for it and store
    # them in a list named area_rect_list.

    def area_calculator(self) -> list[float, float]:

         area_rect_list = [self.width1*self.length1, self.width2*self.length2]
         self.area_rect_list = area_rect_list #storing the list to the object.
         return area_rect_list
    
    # Method: eval_area_similarity(self)
    # Arguments: self
    # Returns: area_similarity_bool (bool): A boolean variables which evaluates to TRUE if both areas are within the relative tolerance, returns FALSE if not.
    # Logic: method inside the class which evaluates the areas in the list of the object area_rect_list. Uses math.isclose to check if
    # both areas are close to each other within the relative tolerance indicated. Returns area_similarity_bool as TRUE/ FALSE.
    # Using the sys library in Python, can get the machine epsilon, the upper bound on approximation error in floating point number systems.
    # Set this value to the relative tolerance - so the values must be within the approximation error range. Relative error used as it determines the tolerance
    # wrt to the area size.
    def eval_area_similarity(self) -> bool:
         area_similarity_bool = math.isclose(self.area_rect_list[0], self.area_rect_list[1], rel_tol=sys.float_info.epsilon)
         return area_similarity_bool
    
# ************************************************************ MAIN FUNCTION ************************************************** #

# Function: main()
# Arguments: none
# Returns: nothing, only shows the parameters on the terminal window.
# Shows: terminal window with TRUE/FALSE for each parameter, indicating if they are a floating point number > 0. If false shown for one or more
# Variable, exits and raises AssertionError. If all variables are correct, will then calculate the area, show it on the terminal, and then indicate if
# The areas are same within a tolerance setup in the above class.
def main():

    # Creating float (python float is implemented as a C double) variables and 
    # using them to store the lengths and widths as Python does not have a double data type.
    # Python number data types are: int, long, float, complex.
    # The variable: float is a hint
    length1 = float(0.3)
    width1 = float(0.6)
    length2 = float(1)
    width2 = float(0.06)

    # Creating a new object using the class rectangle_area_class with the variables inputted.
    variable_obj = rectangle_area_class(length1, length2, width1, width2)
    variable_bool_list = variable_obj.eval_variables()

    print(f"Length 1 dimension validity: {variable_bool_list[0]}\n",
            f"Length 2 dimension validity: {variable_bool_list[1]}\n",
            f"Width 1 dimension validity: {variable_bool_list[2]}\n",
            f"Width 2 dimension validity: {variable_bool_list[3]}\n",)

    # Assert statement checks if all the booleans variables in the variable_bool_list are true - if assertation fails
    # Python raises assertation error giving the error (written next to the assert statement), prints it, then exits the code.
    try:
        assert all(variable_bool_list), "One or more rectangular dimensions are not positive floats"
    except AssertionError as e:
        print(e)
        sys.exit(1)

    area_rect_list = variable_obj.area_calculator()
    area_similarity_bool = variable_obj.eval_area_similarity()

    print(f"The area of the first rectangle is: {area_rect_list[0]}")
    print(f"The area of the second rectangle is: {area_rect_list[1]}")
    print(f"The areas have been evaluated to be the same: {area_similarity_bool}")

# ************************************************************ SCRIPT TO RUN MAIN FUNCTION ************************************************** #

# Running the main function if this program is directly excecuted.
if __name__ == "__main__":
    main()

    #Code for requiring enter to exit to keep terminal window open, as suggested by TA for prior assignment.
    try:
            input("\nPress Enter to exit...")
    except EOFError:
        pass