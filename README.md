# **Assignment 1: "Hello World"**
**Author:** Faheem Saeed  
**Student Number:** 18133158  
**Course:** MECH 524  

## **README Purpose**
The purpose of this readme is to indicate the required dependencies, how to copy the codebase, install all dependencies, and compile it, to allow future developers to contribute.

## **Referenced Material**
ChatGPT used to understand how to format a README.md using # and * for italicization, bolding, different header classes, and how to put code in a readme using `your code here`.
Assignment Guidelines.pdf used to understand how to format the readme, v

## **Codebase Purpose**
The purpose of this codebase is to create a simple executable program in python which prints a given statement, in this case, hello world, to the terminal and stays active there until termination by the user.

## **License**
This work is guarded by the MIT No Attribution License, last updated on May 15, 2020.

## **Change Log**
- <1.0> Initial codebase release on 2025-09-17. Simple executable program to print a statement "Hello World" on terminal.

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
keyboard==0.13.5

## **Installation**
1. Install Python 3.1+, pyinstaller releases support Python 3.7 - 3.12

2. Install an IDE like VSCode

3. Clone the repository via bash
    git clone https://github.com/fsaeed2/M524_HW1.git  
    cd M524_HW1  

4. Create and activate virtual environment, installing all dependencies:

`python -m venv M524`  
`M524\Scripts\activate`  

5. Install dependencies found in requirements.txt

`pip install -r requirements.txt`  

6. If future dependencies added to the project, use `pip freeze > requirements.txt` to update dependency file.

## **Compiling & Execution**
1. Navigate to project folder in your terminal (bash)
2. Run pyinstaller `pyinstaller --onefile main.py`
    This creates a distributable folder `dist/` where the final executable is stored, a `.spec` file containing configuration for future builds, and a `build/` folder for temporary files.
3. If you want to add an icon, use the following method:
`pyinstaller --onefile --icon=app.ico main.py`
4. Double click the `.exe` file in the dist folder to run the application.