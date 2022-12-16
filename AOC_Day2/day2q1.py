

def calculate_score(filename):
    """
    "The first column is what your opponent is going to play: 
    A for Rock, B for Paper, and C for Scissors. 

    The second column, you reason, must be what you should play in response: 
    X for Rock, Y for Paper, and Z for Scissors.

    The score for a single round is the score for the shape you selected 
    (1 for Rock, 2 for Paper, and 3 for Scissors) 
    plus the score for the outcome of the round 
    (0 if you lost, 3 if the round was a draw, and 6 if you won).
    """
    total_score = 0
    with open(filename) as file:

        for line in file:
            round_score = 0
            line.strip()
            opponent_throw = line[0]
            my_throw = line[1]

            if my_throw == "X":
                round_score + 1
            elif my_throw == "Y":
                round_score + 2
            else:
                round_score + 3

            if opponent_throw == "A" and my_throw == "Z":


