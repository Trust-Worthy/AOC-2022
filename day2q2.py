def calculate_score(filename):
    """
    In the first round, your opponent will choose Rock (A), 
    and you need the round to end in a draw (Y), so you also choose Rock. 
    This gives you a score of 1 + 3 = 4.
    In the second round, your opponent will choose Paper (B), 
    and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
    In the third round, you will defeat your 
    opponent's Scissors with Rock for a score of 1 + 6 = 7.

    X means you need to lose, 
    Y means you need to end the round in a draw, 
    and Z means you need to win. 
    """

    with open(filename) as file: 
        total_score = 0
        for line in file:
            line.split()
            line.strip()
            
            round_score = 0
            
            opponent_throw = line[0]
            my_throw = line[2]

            # A is rock 1 point
            # B is paper 2 points
            # C is scissors 3 points

            if my_throw == "X": # X means I need to lose
                if opponent_throw == "A": # A is rock
                    round_score += 3 # is opponent throws rock I would throw scissors two lose
                elif opponent_throw == "B":
                    round_score += 1 # if opponent throws paper I would throw rock to lose
                else:
                    round_score += 2 # if opponent throws scissors I would throw paper to lose   
                total_score += round_score # I get 0 points for losing the roung
            elif my_throw == "Y": # Y means I need to draw
                if opponent_throw == "A": # A is rock
                    round_score += 1 
                elif opponent_throw == "B":
                    round_score += 2
                else: # opp throw is C which is 3 points
                    round_score += 3
                round_score += 3 # drawing a round
                total_score += round_score
            else: # Z means I need to win
                if opponent_throw == "A": # A is rock
                    round_score += 2 
                elif opponent_throw == "B":
                    round_score += 3
                else:
                    round_score += 1
                round_score += 6 # winning a round 
                total_score += round_score

        return total_score

def main():
    total_score = calculate_score("Test_Input/rock_paper.txt")
    print(total_score)

if __name__ == "__main__":
    main()