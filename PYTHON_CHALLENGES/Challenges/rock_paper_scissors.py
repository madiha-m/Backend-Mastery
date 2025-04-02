def rock_paper_scissors(p1, p2):
    hand = {'rock': 0, 'paper': 1, 'scissors': 2}
    results = ['Draw!', 'Player 1 won!', 'Player 2 won!']
    return print(results[hand[p1] - hand[p2]])


rock_paper_scissors(input(), input())
