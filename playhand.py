# built in python 2.7.15
import time
from deuces import Card, Evaluator, Deck
import numpy as np

print("running setting up...")

board = [
    Card.new('As'),
    Card.new('Jh'),
    Card.new('2c')
]
print("printing starting board...")
Card.print_pretty_cards(board)

hand = [
    Card.new('Qd'),
    Card.new('Th')
]
print("printing hand...")
Card.print_pretty_cards(hand)

# set up game parameters
# number of players
#numplayers = input("How many players?")
numplayers = input("How many players?")
numplayers = 4
players = np.zeros(4)

# Start a new deck
deck = Deck()
# Start the Evaluator
evaluator = Evaluator()
# draw 5 cards for the board
board = deck.draw(5)
# draw 2 cards for each of four players
player1_hand = deck.draw(2)
player2_hand = deck.draw(2)
player3_hand = deck.draw(2)
player4_hand = deck.draw(2)

print("\n")

# Print board and hands
print("\n")
print("board:")
Card.print_pretty_cards(board)

# Player 1
print("\n")
print("player 1:")
Card.print_pretty_cards(player1_hand)
# Evaluate hands
p1_score = evaluator.evaluate(board, player1_hand)
print("\n")
print("score:")
print(p1_score)
# bin into classes by rank
p1_class = evaluator.get_rank_class(p1_score)
print("\n")
print("class:")
print(p1_class)
print("\n")
# Player 2
print("\n")
print("player 2:")
Card.print_pretty_cards(player2_hand)
# Evaluate hands
p2_score = evaluator.evaluate(board, player2_hand)
print p2_score
# bin into classes by rank
p2_class = evaluator.get_rank_class(p2_score)
print("\n")
print("class:")
print(p2_class)
print("\n")

# Player 3
print("\n")
print("player 3:")
Card.print_pretty_cards(player3_hand)
# Evaluate hands
p3_score = evaluator.evaluate(board, player3_hand)
print p3_score
# bin into classes by rank
p3_class = evaluator.get_rank_class(p3_score)
print("\n")
print("class:")
print(p3_class)
print("\n")

# Player 4
print("\n")
print("player 4:")
Card.print_pretty_cards(player4_hand)
# Evaluate hands
p4_score = evaluator.evaluate(board, player4_hand)
print(p4_score)
# bin into classes by rank
p4_class = evaluator.get_rank_class(p4_score)
print("\n")
print("class:")
print(p4_class)
print("\n")
print("\n")

print("board:")
Card.print_pretty_cards(board)
print("\n")
print "Player 1 hand rank = %d (%s)\n" % (p1_score, evaluator.class_to_string(p1_class))
Card.print_pretty_cards(player1_hand)
print("\n")
print "Player 2 hand rank = %d (%s)\n" % (p2_score, evaluator.class_to_string(p2_class))
Card.print_pretty_cards(player2_hand)
print("\n")
print "Player 3 hand rank = %d (%s)\n" % (p3_score, evaluator.class_to_string(p3_class))
Card.print_pretty_cards(player3_hand)
print("\n")
print "Player 4 hand rank = %d (%s)\n" % (p4_score, evaluator.class_to_string(p4_class))
Card.print_pretty_cards(player4_hand)
print("\n")


if p1_score > p2_score:
    if p1_score > p3_score:
        if p1_score > p4_score:
            print("Player 1 wins with (%s)" % evaluator.class_to_string(p1_class))
            Card.print_pretty_cards(player1_hand)
        else:
            print("Player 4 wins with (%s)" % evaluator.class_to_string(p4_class))
            Card.print_pretty_cards(player4_hand)
elif p2_score > p3_score:
    if p2_score > p4_score:
        print("Player 2 wins with (%s)" % evaluator.class_to_string(p2_class))
        Card.print_pretty_cards(player4_hand)
    else:
        print("Player 4 wins with (%s)" % evaluator.class_to_string(p4_class))
        Card.print_pretty_cards(player4_hand)
elif p3_score > p4_score:
    print("Player 3 wins with (%s)" % evaluator.class_to_string(p3_class))
    Card.print_pretty_cards(player3_hand)
else:
    print("Player 4 wins! with (%s)" % evaluator.class_to_string(p4_class))
    Card.print_pretty_cards(player4_hand)
