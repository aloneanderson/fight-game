"""Exception file"""


class GameOver(Exception):
    """Method that ends the game and writes the score to a text file"""

    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.write_scores()

    def write_scores(self):
        """function write score to text file"""
        with open('scores.txt', 'a') as file:
            file.write(f'\n\'{self.name}\' with score: {self.score}')


class EnemyDown(Exception):
    """Called when enemy loose"""
    pass
