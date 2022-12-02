#%%
import numpy as np

filename = "rounds.txt"
filename_test = "rounds_test.txt"
round_delimiter = "\n" # Separates different roudns
move_delimiter =  " " # Separates moves

first_moves  = ['A', 'B', 'C'] # Rock, paper, scissors
second_moves  = ['X', 'Y', 'Z'] # Rock, paper, scissors / Loss, draw, win
move_points = [1, 2, 3] # Rock, paper, scissors
outcome_points = [0, 3, 6] # Loss, draw, win

def read_rounds(rounds_file):
    """ Read the text file with the strategy information for each round.
    Return a list of the the two moves for each round """
    rounds = []
    with open(rounds_file, 'r') as file:
        data = file.read().strip() # Read entire dataset
        round_data = data.split(round_delimiter) # Split dataset into rounds
        for rd in round_data:
            rd = rd.strip()
            rd_moves = rd.split(move_delimiter) # Split round into moves
            rounds += [rd_moves]
    return rounds

def score(round, xyz_moves=True):
    """ Return the score for player 2 in the given round 
    Assuming X Y Z represent specific moves (xyz_moves=True)
    or assuming X Y Z represent specific outcomes (xyz_moves=False) """

    def get_outcome(id_diff):
        " Get round outcome for player 2, from the difference in move indices "
        if id_diff == 0: return 1 # Draw
        if id_diff == 1 or id_diff == -2: return 2 # Win
        if id_diff == -1 or id_diff == 2: return 0 # Loss

    def get_second_move(move1_id, outcome):
        " Given a move, get the second move to obtain the given outcome "
        if outcome == 0: id_diff = -1 # Loss
        elif outcome == 1: id_diff = 0 # Draw
        elif outcome == 2: id_diff = 1 # Win
        return (move1_id + id_diff) % 3
    
    move1, move2 = round[0], round[1]
    if move1 not in first_moves or move2 not in second_moves:
        raise ValueError(f"Invalid moves in this round {round}")
    move1_id, move2_id = first_moves.index(move1), second_moves.index(move2)

    if xyz_moves:
        move_pt = move_points[move2_id]
        round_outome = get_outcome(move2_id - move1_id)
        outcome_pt = outcome_points[round_outome]
    else:
        move2_true_id = get_second_move(move1_id, move2_id)
        move_pt = move_points[move2_true_id]
        outcome_pt = outcome_points[move2_id]
    return move_pt + outcome_pt

test_rounds = read_rounds(filename_test)
test_points = sum([score(tr) for tr in test_rounds])
test_points2 = sum([score(tr, xyz_moves=False) for tr in test_rounds])
assert(test_rounds == [['A','Y'], ['B','X'], ['C','Z']])
assert(test_points == 15)
assert(score(['A', 'Y'], xyz_moves=False) == 4 )
assert(score(['B', 'X'], xyz_moves=False) == 1 )
assert(score(['C', 'Z'], xyz_moves=False) == 7 )
assert(test_points2 == 12)

rounds = read_rounds(filename)
points = [score(round) for round in rounds]
points2 = [score(round, xyz_moves=False) for round in rounds]
point_total, point_total2 = sum(points), sum(points2)
print(f"Assuming that X Y Z are moves, the point total after all rounds is {point_total}.")
print(f"Assuming that X Y Z are outcomes, the point total after all rounds is {point_total2}.")

