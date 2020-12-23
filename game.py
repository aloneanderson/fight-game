"""Main executable"""
from models import Enemy, Player
from exceptions import GameOver, EnemyDown


def start():
    """Start function that starts the game, or not:)"""
    g_start = input('Type \'start\' if you wanna play: ')
    if g_start == 'start':
        print('Game BEGINS!!!')
    else:
        print('See you next time!')
        raise SystemExit


def play():
    """function that starts the game play"""
    print('Please type your nickname')
    name = input('Your nickname: ')
    start()
    level = 1
    player = Player(name, 1)
    enemy = Enemy(level)
    print(f'===== level {level} =====')
    while True:
        try:
            print('Your attack')
            choice = input('Your choice: ')
            player.attack(choice, enemy)
            print('Your defence')
            choice = input('Your choice: ')
            player.defence(choice, enemy)
        except EnemyDown:
            level += 1
            print(f'===== level {level} =====')
            player.increase_score()
            enemy = Enemy(level)


if __name__ == '__main__':
    try:
        play()
    except GameOver:
        print('Game Over!')
    except KeyboardInterrupt:
        pass
    finally:
        print('Good Bye!')
