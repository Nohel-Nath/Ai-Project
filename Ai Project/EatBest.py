# Importing required libraries
import random

# Parameters of this game
maxWeight = 250
turn = 3

# Greeting
print('\n\n\tWelcome To BestEat - AI Game!\n')

# Collection of fruits having weight with calorie
fruitsCollection = {'A': {'weight': 100, 'calorie': 100}, 'B': {'weight': 50, 'calorie': 100},
                    'C': {'weight': 25, 'calorie': 75}, 'D': {'weight': 12, 'calorie': 36},
                    'E': {'weight': 100, 'calorie': 400}, 'F': {'weight': 50, 'calorie': 150},
                    'G': {'weight': 25, 'calorie': 50}, 'H': {'weight': 12, 'calorie': 12}}

# Fruit names mapping with numbers
fruitNameNumberMapping = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H'}

# Calorie-Weight ratio of fruits
calorieWeightRation = {}
fruits = fruitsCollection.keys()
for fruit in fruits:
    calorieWeightRation[fruit] = fruitsCollection[fruit]['calorie'] / fruitsCollection[fruit]['weight']

# Game playing
playerScore = 0
playerRemainingWeight = 250

computerScore = 0
computerRemainingWeight = 250

for i in range(turn):
    playerFruitNumber = []
    playerFruitCollection = {}
    playerFruitNumber = random.sample(range(1, 8), 3)

    computerFruitNumber = []
    computerFruitCollection = {}
    computerCalorieWeightRatio = [0] * 8
    computerFruitNumber = random.sample(range(1, 8), 3)

    # Player's turn
    for index in playerFruitNumber:
        playerFruitCollection[fruitNameNumberMapping[index]] = {'weight': fruitsCollection[fruitNameNumberMapping[index]]['weight'],
                                                                'calorie': fruitsCollection[fruitNameNumberMapping[index]]['calorie']}
    
    print('\nPlayer\'s Score: ', playerScore)
    print('\nPlayer\'s Remaining Weight: ', playerRemainingWeight)
    print('\n\t Player (Human)')
    print('---------------------------')
    print('Fruit Name' + '\t' + 'Weight' + '\t\t' + 'Calorie')

    for index in playerFruitNumber:
        print(fruitNameNumberMapping[index], '\t\t\t', playerFruitCollection[fruitNameNumberMapping[index]]['weight'],
              '\t\t\t', playerFruitCollection[fruitNameNumberMapping[index]]['calorie'])

    # Choice handling of player
    playerSelectionOptions = playerFruitCollection.keys()

    playerChoise = input('Enter a fruit name: ')
    playerChoise = playerChoise.capitalize()

    if playerChoise in playerSelectionOptions and (playerRemainingWeight - fruitsCollection[playerChoise]['weight']) >= 0:
        playerRemainingWeight -= fruitsCollection[playerChoise]['weight'];
        playerScore += fruitsCollection[playerChoise]['calorie']
    else:
        print('\nPlayer\'s Remaining Weight Exceeded!\n')
    
    print('\nPlayer\'s Score: ', playerScore)
    print('\nPlayer\'s Remaining Weight: ', playerRemainingWeight)

    # Computer's turn
    for index in computerFruitNumber:
        computerFruitCollection[fruitNameNumberMapping[index]] = {'weight': fruitsCollection[fruitNameNumberMapping[index]]['weight'],
                                                                'calorie': fruitsCollection[fruitNameNumberMapping[index]]['calorie']}
        computerCalorieWeightRatio[index] = calorieWeightRation[fruitNameNumberMapping[index]]
    
    print('\nComputer\'s Score: ', computerScore)
    print('\nComputer\'s Remaining Weight: ', computerRemainingWeight)
    print('\n\t Computer (AI)')
    print('---------------------------')
    print('Fruit Name' + '\t' + 'Weight' + '\t\t' + 'Calorie')

    for index in computerFruitNumber:
        print(fruitNameNumberMapping[index], '\t\t\t', computerFruitCollection[fruitNameNumberMapping[index]]['weight'],
              '\t\t\t', computerFruitCollection[fruitNameNumberMapping[index]]['calorie'])

    # Choice handling of computer
    computerSelectionOptions = computerFruitCollection.keys()
    maxCalorieIndex = computerCalorieWeightRatio.index(max(computerCalorieWeightRatio))
    computerChoice = fruitNameNumberMapping[maxCalorieIndex]

    if computerChoice in computerSelectionOptions and (computerRemainingWeight - fruitsCollection[computerChoice]['weight']) >= 0:
        computerRemainingWeight -= fruitsCollection[computerChoice]['weight'];
        computerScore += fruitsCollection[computerChoice]['calorie']
    else:
        print('\nComputer\'s Remaining Weight Exceeded!\n')
    
    print('\nComputer\'s Choice: ', computerChoice)
    print('\nComputer\'s Score: ', computerScore)
    print('\nComputer\'s Remaining Weight: ', computerRemainingWeight)
    
print('\nPlayer\'s Score: ', playerScore)
print('Player\'s Remaining Weight: ', playerRemainingWeight)
print('\nComputer\'s Score: ', computerScore)
print('Computer\'s Remaining Weight: ', computerRemainingWeight)

if playerScore > computerScore:
    print('\n\nWinner - Player! Congrats!')
elif playerScore < computerScore:
    print('\n\nWinner - Computer! Congrats!')
else:
    print('\n\nScore Label! Match Draw')

