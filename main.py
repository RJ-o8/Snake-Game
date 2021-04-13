from game import Game
import sys

def main():
    game = Game()
    game.run()
    sys.exit()

if __name__ == '__main__':
    main()
    

"""
    BEhaviour:
        Game over:
            -snake touch edge of screen
            -snake touch itself
        snake movement:
            -body trails its head
        snake:
            -eats apple and grow by 1
        score:
            -how many apple eaten
        menu screen:
            -shows at the begenning
            -dissapears at any key press
        game over screen:
            -displays on gameover
            -will go back to a new game on keypress
        key input:
            -arrow keys and wasd change direction of snake

"""

"""
    constants:
        -colors
        -dimensions
        -size of cell
        -speed(frame rate)

"""

# snake is a list of blocks


