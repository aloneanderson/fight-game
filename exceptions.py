class GameOver(Exception):
    def __init__(self, name, score):
        self.name = name
        self.score = score
        with open('scores.txt', 'a') as file:
            file.write(f'\n\'{name}\' with score: {score}')


class EnemyDown(Exception):
    pass
