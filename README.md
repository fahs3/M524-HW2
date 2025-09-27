# **Assignment 2: "Area of Rectangle Calculator"**
**Author:** Faheem Saeed  
**Student Number:** 18133158  
**Course:** MECH 524  

## **README Purpose**
The purpose of this readme is to indicate the required dependencies, how to copy the codebase, install all dependencies, and compile it, to allow future developers to contribute.

## **Referenced Material**
ChatGPT used to understand how to format a README.md using # and * for italicization, bolding, different header classes, and how to put code in a readme using `your code here`.
Assignment Guidelines.pdf used to understand how to format the readme.

## **Codebase Purpose**
The purpose of this codebase is to create a simple executable program in python which serves to calculate the area of the two rectangles given doubles for length and width information. It returns a bool variable `0` for if the areas of the rectangle are the same and `1` if not. It has necessary error handling functionality to indicate if a negative value, a 0, or a non floating point variable has been provided as a rectangle parameter and throws an AssertionError. If the variables provided
are valid, it calculates the area of both rectangles and compares if they are the same. Due to floating point errors as it is difficult to represent a base 10 decimal as a base 2, both areas are compared to determine if they are within a defined relative tolerance. To do this and make the program robust and buildable upon for the future, a class and appropriate methods have been setup, as is common in object oriented programming (OOP).

## **License**
This work is guarded by the MIT No Attribution License, last updated on May 15, 2020.

## **Change Log**
- <1.0> Initial codebase release on 2025-09-24. Simple executable program to calculate area of 2 rectangles, determine

## **Features**
- Inputted statement in main.py printed in terminal when executable is run, and waits for user

## **Dependencies & Frameworks**
pyinstaller==6.0+ (below dependencies for pyinstaller)
    [altgraph==0.17.4
    packaging==25.0
    pefile==2023.2.7
    pyinstaller==6.16.0
    pyinstaller-hooks-contrib==2025.8
    pywin32-ctypes==0.2.3
    setuptools==80.9.0]

The math and sys libraries are included in Python, and so they are not considered as external dependencies.

## **Installation**
1. Install Python 3.1+, pyinstaller releases support Python 3.7 - 3.12

2. Install an IDE like VSCode

3. Clone the repository via bash
    git clone https://github.com/fahs3/M524-HW2.git 
    cd M524-HW2  

4. Create and activate virtual environment, installing all dependencies:

`python -m venv M524`
`M524\Scripts\activate`  

5. Install dependencies found in requirements.txt

`pip install -r requirements.txt`  

6. If future dependencies added to the project, use `pip freeze > requirements.txt` to update dependency file.

## **Debugging Instructions**
Using VSCode or similar, after setting up virtual environment and installing dependencies, the developer can
utilize the debugger to step through the code. This can be done by setting breakpoints by clicking the left of the
row number in main.py, and setting red breakpoints where outputs can be analyzed and code can be stepped through
line by line. To run the debugger, use the keybinding `CTRL+F5` or click the downwards chevron next to the run icon and
press `Python Debugger: Debug Python File.`

## **Tested Platform/ Versions**
1. Operating System: Windows 11
2. Hardware: PC
3. Python Version: Python 3.1+. pyinstaller releases support Python 3.7 - 3.12.

## **Compiling & Execution**
1. Navigate to project folder in your terminal (bash)
2. Run pyinstaller `pyinstaller --onefile main.py`
    This creates a distributable folder `dist/` where the final executable is stored, a `.spec` file containing configuration for future builds, and a `build/` folder for temporary files.
3. If you want to add an icon, use the following method:
`pyinstaller --onefile --icon=app.ico main.py`
4. Move the launcher (RUN ME TO RUN APP).bat to the same folder as the .exe outputted in the `dist/` folder titled main.exe
5. Double click the `launcher (RUN APP).bat` file in the dist folder to run the application.
6. The `launcher (RUN APP).bat` runs the main.exe in a new console window and keeps it open after the output is given.