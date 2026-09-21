RPG Character Builder Program

Overview

This is a Python script designed to create and display custom RPG character stat sheets based on user input. It validates character parameters such as name length, valid stat ranges, and total point distribution, then prints an ASCII-style character card.

Features and Rules

* Character Name: Must be a non-empty string with a maximum of 15 characters and containing no spaces.  
* Stats (Strength, Intelligence, Charisma): Must be integers between 1 and 9 (inclusive).  
* Total Points Rule: The sum of Strength, Intelligence, and Charisma must equal exactly 15 points upon character creation.  
* Visual Output: Displays character stats visually using filled bullet symbols and empty circle symbols to represent stat levels up to 15 points.

Validation Logic

The function checks the inputs against strict rules and returns specific error messages if validation fails:

1. Checks if the name is a string, is not empty, does not exceed 15 characters, and contains no spaces.  
2. Checks if all stats are integer values.  
3. Ensures each individual stat is between 1 and 9\.  
4. Verifies that the total points distributed across Strength, Intelligence, and Charisma equal exactly 15 points.

How to Run

1. Ensure Python 3.x is installed on your computer.  
2. Open your terminal or command prompt.  
3. Run the script using the following command:

python rpg\_character\_build.py

4. Follow the on-screen prompts to enter your character's name and assign points for Strength, Intelligence, and Charisma (1-9).

Built for UTM students\!