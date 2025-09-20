@REM ************************************************************ HEADER ************************************************************
@REM - Assignment 1: Hello World
@REM - Name: Faheem Saeed
@REM - Student ID: 18133158
@REM - File: launcher.c
@REM - Purpose: Contains the code for the launcher.exe, which is used to open main.py in a console window which never terminates itself.
@REM - Description: The code for the launcher.exe, which serves to open up the main.exe in a new window which persists after the hello world
@REM statement has been run, so that output can be seen. Instead of using a .bat file, decided to make it into a .exe file.

@REM ************************************************************ REFERENCED MATERIAL ***********************************************

@REM ChatGPT used for instructions on how to create a new window which persists using C.
@REM Referenced provided header example to setup header.

@REM ************************************************************ DEPENDENCIES ******************************************************

@REM No dependencies required.

@REM ************************************************************ GLOBAL VARIABLES **************************************************

@REM None present

@REM ************************************************************ FUNCTION & CLASS DEFINITIONS **************************************
@REM Command string: start "" cmd /k "main.exe"

@REM Arguments:
@REM start - windows command to launch a new console window
@REM "Application" - string for windows title
@REM cmd - launches a new console window for the command prompt
@REM /k - tells cmd.exe to run the command and then stay open, /c would result in closing the window after running the command
@REM "main.exe" - the command that runs - causes opening of main.exe in the new cmd window and then it stays open after the output.

@REM Returns: nothing
@REM Logic: start opens a new console window - cmd indicates that this window is a command prompt, "Application" string indicates the name for the window
@REM /k prevents it from being closed after running the command "main.exe", thus allowing it to stay open after the output of main.exe is shown.

@echo off
start "main.exe" cmd /k "main.exe"