# Author: Abdallah
# Assesment 4 : ECCLKA ACBT202303 CSP1150A
# Task: Develop Midnight Game

def validateInt(prompt, isSplit=False):
    # Loop indefinitely until valid input is received
    while True:
        # If isSplit is True, split the user input into a list of strings
        if isSplit == True:
            userInput = input(prompt).split(" ")
        else:
            # Otherwise, take the whole input as a single string
            userInput = input(prompt)
        
        valList = []

        # Iterate over each element (or the whole input if not split)
        for i in userInput:
            # Check if the current element is a digit
            if i.isdigit():
                # Convert to integer and add to the valList
                valList.append(int(i))
            else:
                # If not a digit, print error message and restart the loop
                print("Invalid input. Please enter a valid number.")
                continue
        
        # Check if exactly one integer was entered and isSplit is False
        if len(valList) == 1 and isSplit == False:
            # Return the single integer
            return valList[0]
        else:
            # In all other cases (multiple integers or isSplit is True), return the list of integers
            return valList
