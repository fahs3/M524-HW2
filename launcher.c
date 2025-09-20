// ************************************************************ HEADER ************************************************************
// - Assignment 1: Hello World
// - Name: Faheem Saeed
// - Student ID: 18133158
// - File: launcher.c
// - Purpose: Contains the code for the launcher.exe, which is used to open main.py in a console window which never terminates itself.
// - Description: The code for the launcher.exe, which serves to open up the main.exe in a new window which persists after the hello world
// statement has been run, so that output can be seen. Instead of using a .bat file, decided to make it into a .exe file.

// ************************************************************ REFERENCED MATERIAL ***********************************************

// ChatGPT used for instructions on how to create a new window which persists using C.
// I learnt how to use pyinstaller from ChatGPT to bundle the application and its dependencies into an exe file.
// Used ChatGPT for code review - to see if following PEP 8 coding stylization for Python, and determine differences to judge if acceptable or not.
// Referenced provided header example to setup header.

// ************************************************************ DEPENDENCIES ******************************************************

// Install msys2 to install the compiler for the C code (GCC). Add <C:\msys64\ucrt64\bin> to the path environmental variable 
// (or different depending on where you installed msys2 to). 
// This is important as the <stdlib.h> standard library header is a required dependency. It allows usage of general functions such as system(), etc. in the code.

#include <stdlib.h>

// ************************************************************ GLOBAL VARIABLES **************************************************

// None present

// ************************************************************ FUNCTION & CLASS DEFINITIONS **************************************
// Function: int main(void)
// Arguments: void (doesn't take any arguments)
// Returns: 0 (int)
// Logic: system() is a function from stdlib.h header that we included. The code launches a new cmd window to run a command.
// /k indicates to the system to run the command and remain open, the command being main.exe, the main program. Return 0 is convention for success as echo can be used
// to determine the return of the launcher.exe - using echo %ERRORLEVEL%.

int main(void) {
    system("start \"\" cmd /k \"main.exe\"");
    return 0;
}