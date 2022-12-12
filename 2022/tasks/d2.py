from task import Task

conversion = {"X": 0, "Y": 1, "Z": 2, "A": 0, "B": 1, "C": 2}
scores = {
    0: 1,  # rock
    1: 2,  # paper
    2: 3,  # scissors
    3: 6,  # win
    4: 3,  # draw
    5: 0,  # lose
}
wincon = {0: 2, 1: 0, 2: 1}
losecon = {v: k for k, v in wincon.items()}


def match_result(opponent: int, you: int):
    if opponent == you:
        return 4  # draw
    if opponent == wincon[you]:
        return 3  # win
    return 5  # lose


def solve(input: list[str]):
    score1 = 0
    score2 = 0
    for match in input:
        opponent = conversion[match[0]]
        you = conversion[match[2]]
        score1 += scores[you]
        score1 += scores[match_result(opponent, you)]
    #PART TWO
    for match in input:
        opponent = conversion[match[0]]
        you: int
        if match[2] == "X":  # lose
            you = wincon[opponent]
            score2 += scores[5]
        elif match[2] == "Y":  # draw
            you = opponent
            score2 += scores[4]
        else:  # win
            you = losecon[opponent]
            score2 += scores[3]
        score2 += scores[you]
    return score1, score2


task = Task(2, "Rock Paper Scissors", solve)
