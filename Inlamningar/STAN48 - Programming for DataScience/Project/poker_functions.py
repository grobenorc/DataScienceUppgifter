# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 19:41:22 2023

@author: claes
"""


'''
Script for evaluating poker hands. 
https://briancaffey.github.io/2018/01/02/checking-poker-hands-with-python.html/
'''


# %% Checking the hnad for that could be looped thourhg for each player
'''
These are the functions for checking the hands (that will be looped through for each player. 
It return a numeric value of the hand-rank
'''
from collections import defaultdict
from itertools import combinations

card_order_dict = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10,"J":11, "Q":12, "K":13, "A":14}
hand_dict = {9:"straight-flush", 8:"four-of-a-kind", 7:"full-house", 6:"flush", 5:"straight", 4:"three-of-a-kind", 3:"two-pairs", 2:"one-pair", 1:"highest-card"}


def check_straight_flush(hand):
    if check_flush(hand) and check_straight(hand):
        return True
    else:
        return False

def check_four_of_a_kind(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if sorted(value_counts.values()) == [1,4]:
        return True
    return False

def check_full_house(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if sorted(value_counts.values()) == [2,3]:
        return True
    return False

def check_flush(hand):
    suits = [i[1] for i in hand]
    if len(set(suits))==1:
        return True
    else:
        return False

def check_straight(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v] += 1
    rank_values = [card_order_dict[i] for i in values]
    value_range = max(rank_values) - min(rank_values)
    if len(set(value_counts.values())) == 1 and (value_range==4):
        return True
    else:
        #check straight with low Ace
        if set(values) == set(["A", "2", "3", "4", "5"]):
            return True
        return False

def check_three_of_a_kind(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if set(value_counts.values()) == set([3,1]):
        return True
    else:
        return False

def check_two_pairs(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if sorted(value_counts.values())==[1,2,2]:
        return True
    else:
        return False

def check_one_pairs(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if 2 in value_counts.values():
        return True
    else:
        return False




# %% Check what and return value of a hand that a player has


def check_hand(hand):
    if check_straight_flush(hand):
        return 9
    if check_four_of_a_kind(hand):
        return 8
    if check_full_house(hand):
        return 7
    if check_flush(hand):
        return 6
    if check_straight(hand):
        return 5
    if check_three_of_a_kind(hand):
        return 4
    if check_two_pairs(hand):
        return 3
    if check_one_pairs(hand):
        return 2
    return 1




# %%
#exhaustive search using itertools.combinations
def play(cards):
    hand = cards[:5]
    deck = cards[5:]
    best_hand = 0
    for i in range(6):
        possible_combos = combinations(hand, 5-i)
        for c in possible_combos:
            current_hand = list(c) + deck[:i]
            hand_value = check_hand(current_hand)
            if hand_value > best_hand:
                best_hand = hand_value

    return hand_dict[best_hand]


def players_cards(player_lists):
    for i in range(1, len(player_lists) + 1):
        player_name = f'Player {i}'
        hand = player_lists[player_name]
        hand_rank = check_hand(hand)
        print(f"{player_name}: Hand rank: {hand_rank}")


def find_winner(player_lists):
    best_player = None
    best_rank = 0
    best_hand_tail = []

    for player, hand in player_lists.items():
        hand_rank = check_hand(hand)
        hand_tail = sorted(hand[5:], key=lambda x: card_order_dict[x[0]], reverse=True) # It should only look for the highest card on the player's hand.

        if hand_rank > best_rank or (hand_rank == best_rank and hand_tail > best_hand_tail):
            best_player = player
            best_rank = hand_rank
            best_rank_message = hand_dict[best_rank]
            best_hand_tail = hand_tail
            message = 'Player wins on highest card'
            
    # globals()['winner_round'] = best_player #This assign the winner variable the player with the best hand / winner

    return best_player, best_rank_message, best_hand_tail, message
