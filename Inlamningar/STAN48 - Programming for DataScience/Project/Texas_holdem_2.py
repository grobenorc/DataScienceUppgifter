# -*- coding: utf-8 -*-
'''
Created on Mon Oct 16 10:48:53 2023

@author: claes
'''

'''
A simplified program of a Texas Hold'em poker game. As an overview of the functions and running of the program it can be describe as follows:

    # Poker Game Script Overview:
    
    # Initialization
    Check if 'players_chips.csv' exists and load or create a new player chip DataFrame.
    
    # Setting up Player Information
    Ask the user for the number of players.
    Create a dictionary to track players in the current round.
    
    # Dealing Cards
    Initialize and shuffle a deck of cards.
    Deal two cards to each player and display their hands.
    
    # Flop Cards
    Reveal three community cards (the flop) and display them.
    
    # Betting Round
    Players make betting decisions (Call, Fold, Raise, or Check).
    Record bets and player actions.
    
    # Turn Card
    Reveal a single card (the turn) and display it.
    
    # Betting Round (Again)
    Players who are still in the round make more betting decisions.
    Record bets and player actions again.
    
    # River Card
    Reveal the final card (the river) and display it.
    
    # Determining the Winner
    Check player hands and community cards to determine the winner.
    Display the winner and their hand (e.g., "Two Pair" or "Three of a Kind").
    Record the winner for the round.
    
    # Updating Player Chips
    Update player chip counts based on bets made during the round.
    Display the total pot and each player's chip count.
    
    # Game Continuation
    Ask if the user wants to continue playing (yes/no).
    Continue the game or end it based on the user's choice.
    
    # Recursion and Loop
    The game continues in a loop as long as the user chooses to play more rounds.

'''

# %% Preamble
import numpy as np
import random
import pandas as pd
import os
os.chdir('xxx')

# %% Card deck
def generate_card_deck():
    '''
    This function generates a standard deck of playing cards with four suits and thirteen ranks.

    It creates a DataFrame representing a deck with 'Suits' and 'Ranks' columns.

    Returns:
    cards_df (DataFrame): A DataFrame containing the deck of cards.
    '''
    # Create an array of suits (CLUB, DIAMOND, HEART, SPADE) repeating each suit 13 times.
    Suits = np.repeat(['CLUB', 'DIAMOND', 'HEART', 'SPADE'], 13)
    
    # Create an array of ranks (2, 3, 4, 5, 6, 7, 8, 9, T, J, Q, K, A) tiled four times for each rank.
    Ranks = np.tile(['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'], 4)
    
    # Combine the 'Suits' and 'Ranks' arrays to create a DataFrame representing the card deck.
    cards_df = pd.DataFrame({'Suits': Suits, 'Ranks': Ranks})
    
    return cards_df
    


# %% Global environments variables
'''
For us being able to run the script the program has to have information about some of the variables that we will later mutate.

    card_deck: card_deck is used above in order to create a normal deck of cards. This will NOT be mutated during the program is run.
    available_cards: this is a deck of cards which will be mutated once the the cards are shuffled to different players and on the deck (dealer). 
'''
card_deck = generate_card_deck() # Create the original deck of cards
available_cards = generate_card_deck().copy() # Create a copy of the original deck that will be mutated for every time we draw cards to players/river.
cards_on_deck = pd.DataFrame(columns = ['Player/River', 'Suits', 'Ranks']) # This is used for being able to track which cards is at the deck (meaning players hands or on the table/dealer).


players_hand = pd.DataFrame(columns = ['Player', 'Suits', 'Ranks'])
player_in_round = {} # This will be a dictionairy containing of n, number ofp players indicating if the player has fold, or still in the game.
players_chips = pd.DataFrame(columns = ['Player', 'Tot_chips'])
players_bets = pd.DataFrame(columns = ['Player']) #, 'Tot_Bets'])


dealer_hand = pd.DataFrame(columns = ['Dealer', 'Suits', 'Ranks'])

player_lists = {} # This will be used for storing each players hands as well as the the cards on deck


winner_round = ''

# %% Randomize card function
def random_card(cards_df):
    ''' This function randomly selects a card from a given DataFrame of cards.

    Parameters:
    cards_df (DataFrame): A DataFrame containing cards to choose from.

    Returns:
    Series: A single row (card) from the input DataFrame.
    '''
    # Generate a random index within the valid range of DataFrame indices
    random_index = random.randint(0, len(cards_df) - 1)
    # The upper bound is set to len(cards_df) - 1 to match the highest valid index.
    # DataFrame indices are zero-based (0 to len(cards_df) - 1).
    
    return cards_df.iloc[random_index]


# random_card(available_cards)

# %% Dictionairy with boolean value if player in round
def player_in_round_dictionary():
    '''
    This function initializes a dictionary representing players in the current round.

    Parameters:
    None (user input is used to determine the number of players)

    Returns:
    None, it instead changes the global variable with as many player that is chosen that is an indicator if a player has folded, or is still in the game. (variable: player_in_round)
    '''
    # Get the number of players from user input
    number_players_start = int(input('How many players are playing? '))
    print("")

    # Create a dictionary with player names and set them all to True (in the round)
    player_dict = {'Player ' + str(i): True for i in range(1, number_players_start + 1)}
    # The dictionary is created with player names as keys and all initially set to True since everyone starts the game.

    # Update the global 'player_in_round' variable to represent the chosen number of players
    globals()['player_in_round'] = player_dict
    # Changes the original 'player_in_round' variable to match the number of players chosen.

# player_in_round_dictionary()

# %% Creating Dataframe of each players chip count
def player_chips_dataframe(initial_chips=1000):
    '''
    This function initializes a DataFrame to track players' available chips.

    Parameters:
    initial_chips (int, optional): The initial number of chips for each player. Default is 1000.

    Returns:
    None, same as the pleyer_in_round function. It appends as many players that was chosen with chip-count to the global variable.
    '''
    # Get the number of players from the 'player_in_round' global variable
    num_players = len(globals()['player_in_round'])
    
    # Create player data with player names and initial chip amounts
    player_data = {'Player': ['Player ' + str(i) for i in range(1, num_players + 1)],
                  'Tot_chips': [initial_chips] * num_players}
    
    # Create and store the DataFrame for player chips in the 'players_chips' global variable
    globals()['players_chips'] = pd.DataFrame(player_data)
    # The DataFrame is created with player names as 'Player' and initial chip amounts as 'Tot_chips'.

# player_chips_dataframe()


# %% Creating Dataframe of each players chip count
def player_bets_dataframe(initial_bets=0):
    '''
    This function initializes a DataFrame to track players' initial bets (e.g., blinds).

    Parameters:
    initial_bets (int, optional): The initial bet amount (e.g., blinds) for each player. Default is 0.

    Returns:
    None, but same as the previous two functions.
    '''
    # Get the number of players from the 'player_in_round' global variable
    num_players = len(globals()['player_in_round'])
    
    # Create player data with player names and initial bet amounts
    player_data = {'Player': ['Player ' + str(i) for i in range(1, num_players + 1)],
                  'initial_bet': [initial_bets] * num_players}
    
    # Create and store the DataFrame for player bets in the 'players_bets' global variable
    globals()['players_bets'] = pd.DataFrame(player_data)
    # The DataFrame is created with player names as 'Player' and initial bet amounts as 'initial_bet'.

# player_bets_dataframe()



# %% Betting function
'''
Here we have a function that will be used for the betting part of each round. It is therefore 
looking for if a player is in the round, meaning that the player has not folded earlier.
It should also check that the bet is >= to the previus betted player of that round.
'''
def betting_round():
    '''
    This function manages a betting round in a poker game, allowing players to take actions such as call, fold, raise, or check.

    Parameters:
    None (uses global variables for player data and bets)

    Returns:
    None
    '''
    global player_in_round
    global players_chips
    global players_bets

    # Calculate the round number based on the existing bets
    bet_round = players_bets.shape[1] - 1  

    # Create a DataFrame to track player bets in this round
    player_bets_this_round = pd.DataFrame(columns=['Player', 'Bets'])
    player_bets_this_round['Player'] = players_chips['Player']
    player_bets_this_round['Bets'] = 0

    # Initialize the last bet to 0
    last_bet = 0

    for player, in_round in player_in_round.items():
        if in_round:
            valid_bet = False
            while not valid_bet:
                try:
                    action = input(f"{player}, choose your action (Call, Fold, Raise, or Check): ")
                    if action.lower() == "fold":
                        player_in_round[player] = False  # Player folds
                        valid_bet = True
                    elif action.lower() == "call":
                        if last_bet == 0:
                            print("You must make a Raise, Fold, or Check as there is no previous bet.")
                        else:
                            call_amount = last_bet - player_bets_this_round.loc[player_bets_this_round['Player'] == player, 'Bets'].values[0]
                            if call_amount <= players_chips.loc[players_chips['Player'] == player, 'Tot_chips'].values[0]:
                                players_chips.loc[players_chips['Player'] == player, 'Tot_chips'] -= call_amount
                                player_bets_this_round.loc[player_bets_this_round['Player'] == player, 'Bets'] += call_amount
                                valid_bet = True
                            else:
                                print(f"Not enough chips to call. Available: {players_chips.loc[players_chips['Player'] == player, 'Tot_chips'].values[0]}. You must fold or bet a lower amount.")
                    elif action.lower() == "raise":
                        try:
                            raise_amount = int(input(f"How much would you like to raise, {player}? "))
                            if raise_amount >= last_bet:
                                if raise_amount <= players_chips.loc[players_chips['Player'] == player, 'Tot_chips'].values[0]:
                                    players_chips.loc[players_chips['Player'] == player, 'Tot_chips'] -= raise_amount
                                    player_bets_this_round.loc[player_bets_this_round['Player'] == player, 'Bets'] += raise_amount
                                    last_bet = raise_amount
                                    valid_bet = True
                                else:
                                    print(f"Not enough chips to raise. Available: {players_chips.loc[players_chips['Player'] == player, 'Tot_chips'].values[0]}. Please enter a lower raise amount.")
                            else:
                                print("Invalid raise amount. You must raise by at least the previous bet amount or fold.")
                        except ValueError:
                            print("Invalid input. Please enter a valid raise amount.")
                    elif action.lower() == "check":
                        if last_bet == 0:
                            valid_bet = True  # Allow checking if there is no previous bet
                        else:
                            print("You cannot check when there is a previous bet. Please call, fold, or raise.")
                    else:
                        print("Invalid action. Choose 'Call', 'Fold', 'Raise', or 'Check'.")
                except ValueError:
                    print("Invalid input. Please enter a valid bet or 0 to fold.")

    # After the first round of bets, check for players who bet below the maximum
    for index, row in player_bets_this_round.iterrows():
        if row['Bets'] < last_bet:
            valid_bet is False
            while not valid_bet:
                try:
                    if player_in_round[row['Player']]:
                        action = input(f"{row['Player']}, choose your action (Call, Fold, Raise, or Check): ")
                        if action.lower() == "fold":
                            player_in_round[row['Player']] = False  # Player folds
                            valid_bet = True
                        elif action.lower() == "call":
                            valid_bet = True
                            call_amount = last_bet - row['Bets']  # Calculate the amount to call
                            if call_amount <= players_chips.loc[players_chips['Player'] == row['Player'], 'Tot_chips'].values[0]:
                                players_chips.loc[players_chips['Player'] == row['Player'], 'Tot_chips'] -= call_amount
                                player_bets_this_round.loc[player_bets_this_round['Player'] == row['Player'], 'Bets'] += call_amount
                            else:
                                print(f"{row['Player']} does not have enough chips to call. Available: {players_chips.loc[players_chips['Player'] == player, 'Tot_chips'].values[0]}. Please fold or bet a lower amount.")
                        elif action.lower() == "raise":
                            try:
                                raise_amount = int(input(f"How much would you like to raise, {row['Player']}? "))
                                if raise_amount >= last_bet - row['Bets']:
                                    if raise_amount <= players_chips.loc[players_chips['Player'] == row['Player'], 'Tot_chips'].values[0]:
                                        players_chips.loc[players_chips['Player'] == row['Player'], 'Tot_chips'] -= raise_amount
                                        last_bet = row['Bets'] + raise_amount
                                    else:
                                        print(f"{row['Player']} does not have enough chips to raise. Available: {players_chips.loc[players_chips['Player'] == player, 'Tot_chips'].values[0]}. Please enter a lower raise amount.")
                                else:
                                    print(f"Invalid raise amount for {row['Player']}. You must raise by at least the previous bet amount or fold.")
                            except ValueError:
                                print(f"Invalid input for {row['Player']}. Please enter a valid raise amount.")
                        elif action.lower() == "check":
                            if last_bet == 0:
                                valid_bet = True  # Allow checking if there is no previous bet
                            else:
                                print(f"{row['Player']} cannot check when there is a previous bet. Please call, fold, or raise.")
                        else:
                            print(f"Invalid action for {row['Player']}. Choose 'Call', 'Fold', 'Raise', or 'Check'.")
                    else:
                        valid_bet = True  # Skip asking players who have folded
                except ValueError:
                    print(f"Invalid input for {row['Player']}. Please enter a valid bet or 0 to fold.")

    # Add a new column for this round to the players_bets DataFrame
    players_bets[f'bet_round_{bet_round}'] = player_bets_this_round['Bets']

    
 
# Start the betting round
# betting_round()



# %% Function generating first 2 cards for all opponents as well as dealers hand (flop, turn, river)

def cards_for_players(card_deck):
    '''
    This function deals two cards to each player in the game.

    Parameters:
    card_deck (DataFrame): The deck of cards from which cards will be drawn.

    Returns:
    DataFrame: A DataFrame containing the cards dealt to each player.
    '''
    number_players_start = len(globals()['player_in_round'])
    available_cards = card_deck.copy()  # Create a copy of the card deck to prevent modifying the original
    players_hand = pd.DataFrame(columns=['Player', 'Suits', 'Ranks'])

    for i in range(2):
        for j in range(len(globals()['player_in_round'])):
            drawn_card = random_card(available_cards)  # Draw a card randomly from the deck
            available_cards = available_cards.drop(drawn_card.name)  # Remove the drawn card from the deck

            player_name = str(j + 1)
            suit = drawn_card[0]
            rank = drawn_card[1]
            new_row = {'Player': 'Player ' + player_name, 'Suits': suit, 'Ranks': rank}
            index = i * number_players_start + j
            players_hand.loc[index] = new_row

    players_hand = players_hand.sort_values(by=['Player'])
    globals()['available_cards'] = available_cards  # Update the available cards globally for future sampling
    globals()['players_hand'] = players_hand
    return players_hand


# players_hand = cards_for_players(generate_card_deck())


 

def flop_cards(available_cards):
    '''
    This function draws three cards from the available deck to form the flop.

    Parameters:
    available_cards (DataFrame): The deck of cards from which to draw the flop.

    Returns:
    DataFrame: A DataFrame containing the flop cards.
    '''
    available_cards = available_cards  # This line is not necessary, as it's not affecting the function

    flop_hand = pd.DataFrame(columns=['Dealer', 'Suits', 'Ranks'])

    for i in range(3):
        drawn_river_cards = random_card(available_cards)
        available_cards = available_cards.drop(drawn_river_cards.name)

        suit = drawn_river_cards[0]
        rank = drawn_river_cards[1]
        new_row = {'Dealer': 'River ' + str(i + 1), 'Suits': suit, 'Ranks': rank}
        index = i + 1  # Find the index for appending the river cards
        flop_hand.loc[index] = new_row

    globals()['available_cards'] = available_cards  # Update the available cards globally
    globals()['dealer_hand'] = flop_hand  # Update the dealer's hand with the flop cards
    return flop_hand



def turn_river_card(available_cards):
    '''
    This function draws either the turn or river card from the available deck.

    Parameters:
    available_cards (DataFrame): The deck of cards from which to draw the card.

    Returns:
    Series: The card drawn (either turn or river).
    '''
    new_index = len(globals()['dealer_hand'])  # Get the current index in the dealer's hand DataFrame

    card_generated = random_card(available_cards)  # Draw a card from the available deck
    suit = card_generated['Suits']  # Extract the suit from the drawn card
    rank = card_generated['Ranks']  # Extract the rank from the drawn card

    # Determine if it's the turn or river card
    type_card = 'Turn' if new_index == 3 else 'River'

    # Append the new card to the dealer_hand DataFrame
    dealer_hand.loc[new_index + 1] = {'Dealer': str(type_card), 'Suits': suit, 'Ranks': rank}

    # Remove the drawn card from available_cards
    available_cards = available_cards.drop(card_generated.name)

    globals()['available_cards'] = available_cards  # Update the available cards globally

    return card_generated

    
    
    


# river_hand = turn_river_card(available_cards) # Here we use the available cards that has not recently been drawn


# %% Mutate the player_lists dictionairy
def create_player_lists(dealer_hand, players_hand, player_in_round):
    '''
    This function creates a dictionary of player hands for those who are still in the round.

    Parameters:
    dealer_hand (DataFrame): The dealer's hand, including flop, turn, and river cards.
    players_hand (DataFrame): The players' hands.
    player_in_round (dict): A dictionary indicating which players are still in the round.

    Returns:
    dict: A dictionary where keys are player names, and values are lists of card combinations.
    '''
    global player_lists  # Declare that you are modifying the global variable

    # Combine the dealer's hand and players' hands into a single DataFrame
    df = pd.DataFrame(np.vstack([dealer_hand.iloc[0:], players_hand.iloc[0:, :3]]), columns=['id', 'Suits', 'Rank'])

    # Create a 'SuitRank' column by concatenating 'Rank' and the first character of 'Suits'
    df['SuitRank'] = df['Rank'] + df['Suits'].astype(str).str[0]
    df = df.drop(columns=['Suits', 'Rank'])

    player_lists = {}  # Initialize an empty dictionary to store player hands

    # Iterate through unique player names and create a card list for each player still in the round
    for player in df[df['id'].str.startswith('Player')]['id'].unique():
        if player_in_round.get(player, False):
            player_data = df[df['id'].str.startswith(player) | df['id'].isin(['River 1', 'River 2', 'River 3', 'Turn', 'River'])]
            card_list = player_data['SuitRank'].tolist()
            player_lists[player] = card_list

    return player_lists



# %% Evaluate earnings

def players_chips_update():
    '''
    This function updates players' chip counts after a round.

    It calculates the total bets, finds the winner player, and adds the total bets to the winner's chips.
    
    It also prints the total pot and each player's total chips after losses/earnings.

    Global Variables Used:
    - players_chips: DataFrame containing players' chip counts.
    - players_bets: DataFrame containing players' bets in the current round.
    - winner_round: The winner of the round.

    Returns:
    None
    '''
    global players_chips
    global players_bets
    global winner_round

    # Sum the bets for all players in all rounds
    total_bets = players_bets.iloc[:, 1:].sum().sum()

    # Find the winner player for the current round
    winner_player = winner_round

    # Add the total bets to the winner's chips
    winner_chips_index = players_chips['Player'] == winner_player
    players_chips.loc[winner_chips_index, 'Tot_chips'] += total_bets
    
    print('Total pot this round was: ', total_bets)
    print('')
    print('Each player\'s total chips after losses/earnings: \n')
    print(players_chips.to_string(index=False))


# %% Complete game

'''
Overview of function:
    1. Initialize deck of cards
    2. Randomize 2 cards to each player in the game (cards_for_players)
    3. Randomize the cards of the dealer, meaning 3 cards
    4. Let each player bet (betting_function)
    5. Turn over 1 more card
    6. Let each player bet (betting_function)
    7. Turn over 1 more card
    8. Evaluate the winner
    9. Calculate earnings
    10. Update Chips dataframe
    
'''
# Here we have to import the function from the other script called poker_functions. It is a script used to find the winner of the game.
# Make sure the script is located in the correct/below directory
runfile('poker_functions.py') # Import functions from the other that evaluates the hands for each player.

def poker_game():
    '''
    This function represents a round of a poker game. It manages the game's flow, including dealing cards,
    player betting, revealing community cards, determining the winner, and updating player chips.

    Global Variables Used:
    - players_chips: DataFrame containing players' chip counts.
    - player_in_round: Dictionary tracking players still in the round.
    - dealer_hand: DataFrame containing the dealer's cards.
    - available_cards: DataFrame containing remaining cards to draw.
    - players_hand: DataFrame containing players' cards.
    - players_lists: Dictionary mapping players to their card lists.
    - winner_round: The winner of the current round.

    Returns:
    None
    '''
    
    # Check if the CSV file exists
    if os.path.isfile('players_chips.csv'):
        players_chips = pd.read_csv('players_chips.csv')
        delete_csv = True  # Flag to delete the file later
    else:
        player_chips_dataframe()  # Initialize the DataFrame if the file doesn't exist
        delete_csv = False  # No need to delete a newly created file
    
    player_in_round_dictionary()  # Initialize an empty dictionary consisting of key:value --> 'Player_id':True/False
    player_chips_dataframe()  # Initialize a DataFrame consisting of columns 'Player_id', 'Available_chips'
    player_bets_dataframe()  # Initialize an empty DataFrame for keeping track of players' bets each round
    
    # Generate two cards for each of the players, count chosen when calling: player_in_round_dictionary
    cards_for_players(generate_card_deck())  # Shuffle two cards and assign the global variable 'players_hand'.
    
    # Print the cards for each player
    print("======================== Players hands ========================")
    print('\t', globals()['players_hand'].to_string(index=False))
    print("===============================================================\n\n")
    
    # Generate the flop 3-cards
    global dealer_hand
    dealer_hand = flop_cards(globals()['available_cards'])
    
    print('========================= Dealer flop =========================')
    print('\t', globals()['dealer_hand'])
    print("===============================================================\n\n")
    
    # Now each player lays their bets
    betting_round()
    
    # 1 card after the bet, (the turn) 
    turn_card = turn_river_card(globals()['available_cards'])
    print('\n\n========================= Dealer turn =========================\n')
    print(turn_card)
    print("===============================================================\n\n")

    # Each player that is still in the game is now to bet
    betting_round()

    # After the bets have been done, the last card is drawn    
    river_card = turn_river_card(globals()['available_cards'])
    print('========================= Dealer turn =========================')
    print(river_card)
    print("===============================================================\n\n")

    print('======================== Cards on deck ========================')
    print(globals()['dealer_hand']) 
    print("===============================================================")
    
    # Before we can determine the winner, we have to append the player_lists of the players' hands.
    create_player_lists(globals()['dealer_hand'], globals()['players_hand'], globals()['player_in_round'])
    print('===============================================================')
    print('\t\t\t\t And the WINNER is:\n\n')
    print(find_winner(globals()['player_lists'])[0], 'with a', find_winner(globals()['player_lists'])[1], '.')
    print()
    globals()['winner_round'] = find_winner(globals()['player_lists'])[0]
    
    # Now update the players' chips after the round
    print('===============================================================')
    players_chips_update()
    
    continue_game = input("Do you want to continue the game (yes/no)? ").strip().lower()

    if continue_game == "yes":
        poker_game()  # Continue the game by calling the function recursively
    else:
        if delete_csv:
            # Delete the CSV file
            os.remove('players_chips.csv')
        print("Game over. Thanks for playing!")

    
    
    
    
    
    



# %% Play game

poker_game()



