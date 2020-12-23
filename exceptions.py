"""Exception file"""


class GameOver(Exception):
    """Method that ends the game and writes the score to a text file"""

    def __init__(self, name, score):
        self.name = name
        self.score = score
        with open('scores.txt', 'a') as file:
            file.write(f'\n\'{name}\' with score: {score}')


class EnemyDown(Exception):
    """EnemyDown class has no functional"""
    pass
