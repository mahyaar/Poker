from deuces.deuces import Card, Evaluator




def main():

    board = [
        Card.new('Th'),
        Card.new('Jh'),
        Card.new('Qs'),
        Card.new('Ah'),
        Card.new('9d')
    ]
    #board = []

    hand = [
        Card.new('As'),
        Card.new('Ad'),
    ]
    hand_2 = [
        Card.new('Ks'),
        Card.new('Jh'),
    ]
    hand_3 = [
        Card.new('2s'),
        Card.new('Jd'),
    ]
    hands = [hand,hand_2,hand_3]
    hands = [hand]
    init_hands_length = len(hands)
    #Card.print_pretty_cards(board + hand)
    evaluator = Evaluator()
    #print evaluator.evaluate(hand, board,True)
    #print evaluator.hand_summary(board,hands,True)
    winner_count = evaluator.winner_determination(board,hands,5,False)
    total = 0
    for i in range(len(winner_count)):
        total+=winner_count[i]
    prob = [float(count)/total for count in winner_count]
    #print(prob[:init_hands_length])
    print(prob)


main()

