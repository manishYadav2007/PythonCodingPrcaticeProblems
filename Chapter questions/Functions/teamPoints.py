


def get_team_points(wins, draw, loss):
    return (wins * 4) + (draw * 2) + (loss * (-1))



wins, draw, loss = list(map(int, input("Enter the team points: ").split()))

result = get_team_points(wins, draw, loss)
print(result)









