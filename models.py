import random

from exceptions import GameOver, EnemyDown
from settings import GAME_CASES


class Enemy:
    def __init__(self, level):
        self.level = level
        self.lives = self.level

    @staticmethod
    def select_attack():
        return random.randrange(1, 4)

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            raise EnemyDown()


class Player:
    def __init__(self, name, lives):
        self.name = name
        self.lives = lives
        self.score = 0

    def increase_score(self):
        self.score += 5

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            print('You lost')
            raise GameOver(self.name, self.score)

    @staticmethod
    def fight(attack, defence):
        print(attack, defence)
        if attack == defence:
            return 0
        else:
            return GAME_CASES.get((attack, defence))

    def attack(self, player_attack, enemy_obj):
        enemy_defence = enemy_obj.select_attack()
        print(enemy_defence)
        result = self.fight(int(player_attack), enemy_defence)
        if result == 1:
            enemy_obj.decrease_lives()
            print('Your attack was successful!')
        elif result == -1:
            print('You missed')
        else:
            print('Draw')

    def defence(self, player_defence, enemy_obj):
        enemy_attack = enemy_obj.select_attack()
        print(enemy_attack)
        result = self.fight(enemy_attack, int(player_defence))
        if result == 1:
            self.decrease_lives()
            print('You lost')
        elif result == -1:
            print('Your defend was successful!')
        else:
            print('Draw')
