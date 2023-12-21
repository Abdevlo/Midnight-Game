# Author: Abdallah
# Assesment 4 : ECCLKA ACBT202303 CSP1150A
# Task: Develop Midnight Game

# Import propietary random method for dice selection( View MidnightDice function to see import in use)
import random
# Import custom error handling to handle prompt validation ( View MidnightDice function to see import in use)
import validate

# Funtion to display starting screen
def TitleRules():
	# Prints the title and Rules of the games
    print("\n\t\tWelcome to Midnight Dice Game\n")
    print("Rules:")
    print("1. Roll the dice and choose at least one to keep.")
    print("2. If you get both 1 and 4, the remaining dice will be summed up for your score.")
    print("3. Continue rolling until all dice are used.")
    print("4. The player with the highest total score wins.\n")
    print("\n\t\t GOOD LUCK !!\n\n")

# Function to instantiate gameplay
def InitGamePlay():
    # Create an empty dictionary to store player information
    players = {}
    # Get the number of players from user input using the validateInt function
    noOfPlayers = validate.validateInt("Enter number of players:")
    # Initialize a counter for player IDs
    playerCount = 0
    # Iterate through the range of playerCount from 0 to noOfPlayers (exclusive)
    for playerCount in range(noOfPlayers):
        # Increment playerCount for each player
        playerCount += 1
        # Call the MidnightDice function to initialize player information
        MidnightDice(players, playerCount)
    # After all players are initialized, find and display the winner
    FindWinner(players)

# Function for main gameplay logic
def MidnightDice(players, playerCount):
    # Initialize lists to keep track of all dice rolls and the kept dice
    main = []
    mainKeep = []
    # Set the initial number of dice
    dice = 6
    # Initialize player's score
    score = 0
    # Get player's name
    player = input(f"\n\nPlayer {playerCount} Name : ")
    # Main game loop
    while True:
        # Display the dice that have been kept so far
        print(f"\n\t\t Your Keep: {mainKeep}\n")
        # Player's choice to roll or quit
        roll = validate.validateInt("1. Roll\n2. Quit\n\nEnter Your Choice : ")
        # If player chooses to roll
        if roll == 1:
            # List to store the outcomes of this roll
            outComes = []
            # Roll each dice and append its outcome
            for chance in range(dice):
                outComes.append(random.randrange(1, 7))
            main.append(outComes)
            print("\n\t\t", outComes)
            # Ask the player to choose which dice to keep
            keep = validate.validateInt("\nDice you wanna choose. You should Choose at least ONE (KEEP SPACES IN BETWEEN CHOICES) : ", True)
            # Process each chosen dice
            for choice in keep:
                if int(choice) in outComes:
                    mainKeep.append(int(choice))
                    dice -= 1
                else:
                    # Handle invalid choice and exit the game
                    print("Invalid choice")

        # If player chooses to quit
        elif roll == 2:
            DisposeGamePlay()
        # Handle invalid option
        elif roll > 2:
            print("Invalid Option")
            DisposeGamePlay()
        # Break out of the loop when no dice are left
        if dice <= 0:
            break

    # Display the final kept dice
    print("\n\n\n\t\t", mainKeep)
    # Check if both 1 and 4 are in the kept dice
    if 1 in mainKeep and 4 in mainKeep:
        # Remove 1 and 4 and calculate score
        mainKeep.remove(1)
        mainKeep.remove(4)
        score = sum(mainKeep)
        print("\n\n\n" + player + "'s score is  ", sum(mainKeep))
    else:
        # If 1 and 4 aren't both kept, score is 0
        print("Your choice doesn't have 1 and 4. So your points are 0")
        score = 0
    # Update the players dictionary with the player's score
    players[player] = score

# Function to find the winner
def FindWinner(players):
    # Check if the players dictionary is empty
    if not players:
        print("No players in the game.")
        return
    # Find the highest score among all players
    highestScore = max(players.values())
    # Check if the highest score is 0, implying no one scored any points
    if highestScore == 0:
        print("No winners this time. Everyone scored 0.")
        return
    # Create a list of players who have the highest score
    winner = [player for player, score in players.items() if score == highestScore]
    # Check if there is only one winner
    if len(winner) == 1:
        print(f"\n\t\tThe winner is {winner[0]} with a score of {highestScore}.")
    else:
        # If there are multiple winners, join their names in a string
        jointWinners = ', '.join(winner)
        print(f"It's a tie between {jointWinners} with a score of {highestScore}.")

# Function to dispose gameplay instance
def DisposeGamePlay():
    # Loop to ask the user whether to continue or quit
    while True:
        # Prompt user to choose between continuing and quitting
        cont = validate.validateInt("\n\n1. Continue\n2. Quit \nPlay Another Game(a new moon arises) : ")
        # If the user chooses to continue, start a new game
        if cont == 1:
            InitGamePlay()
        else:
            # If the user chooses to quit, break out of the loop, ending the function
            break

def main():
    # Display the title and rules of the game (assuming TitleRules is defined elsewhere)
    TitleRules()
    # Start the initial gameplay
    InitGamePlay()
    # Handle post-gameplay, whether to continue or quit
    DisposeGamePlay()

# Call the main function to start the game
main()