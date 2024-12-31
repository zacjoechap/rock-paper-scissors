# rock-paper-scissors-lizard-spock

# key:
#   move 1 and move 2 separated by a space,
#   in alphabetical order
# value:
#   does move 1 beat move 2?
MOVES = {
    'lizard paper': True,
    'lizard rock': False,
    'lizard scissors': False,
    'lizard spock': True,
    'paper rock': True,
    'paper scissors': False,
    'paper spock': True,
    'rock scissors': True,
    'rock spock': False,
    'scissors spock': False
}

def beats(m1, m2):
    if m1 == m2:
        return None
    elif m1 > m2:
        return not beats(m2, m1)
    else:
        return MOVES[m1 + ' ' + m2]

def main():
    while True:
        try:
            m1 = input('P1: ').strip().lower()
            m2 = input('P2: ').strip().lower()
            result = beats(m1, m2)
            if result is None:
                print('Tie!')
            elif result:
                print('Player 1 wins!')
            else:
                print('Player 2 wins!')
            print()
        except Exception as e:
            print('Invalid comparison\n')

main()
