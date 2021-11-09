from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker


rules={
    (1,1):100,
    (5,1):50,
    (1,3):1000,
    (1,4):2000,
    (1,5):3000,
    (1,6):4000,
    (2,3):200,
    (2,4):400,
    (2,5):600,
    (2,6):800,
    (3,3):300,
    (3,4):600,
    (3,5):900,
    (3,6):1200,
    (4,3):400,
    (4,4):800,
    (4,5):1200,
    (4,6):1600,
    (6,6):2400,
    (6,5):1800,
    (6,4):1200,
    (6,3):600,
    (5,6):2000,
    (5,5):1500,
    (5,4):1000,
    (5,3):500,
    (1,2):200,
    (2,2):0,
    (3,2):0,
    (4,2):0,
    (5,2):100,
    (6,2):0,
    (2,1):0,
    (3,1):0,
    (4,1):0,
    (6,1):0,
}      
class Game():
    def __init__(self,roller=None):
        self.roller = roller
    def play(self):
        counter = 1
        print('Welcome to Game of Greed')
        wanna_play=(input('Wanna play? '))
        if (wanna_play =='n'):
            print('OK. Maybe another time')
        else:
            object = Banker()
            banked = 0
            while counter:
                roundBanked = 0
                print(f'Starting round {counter}')
                print('Rolling 6 dice...')
                roll_dice = self.roller(6)
                nums=[]
                for i in roll_dice:
                    nums.append(str(i))
                print(','.join(nums))
                decide = input('Enter dice to keep (no spaces), or (q)uit: ')
                score = 0
                if decide != 'q':
                    var = tuple(int(i) for i in decide) 
                    # print(var)
                    score = GameLogic.calculate_score(var)
                    length = 6 -len(var)
                    variable= ''.join(sorted(nums))
                    if  decide not in variable:
                        print('Cheater!!! Or possibly made a typo...')
                        print(','.join(nums))
                        decide = input('Enter dice to keep (no spaces), or (q)uit: ')
                        var = tuple(int(i) for i in decide) 
                        score = GameLogic.calculate_score(var)
                        length = 6 -len(var)
                    print(f'You have {score} unbanked points and {length} dice remaining')
                    bank = input('(r)oll again, (b)ank your points or (q)uit ')
                    if bank == 'b':
                        # object = Banker()
                        shelf = object.shelf(score)
                        banked = object.bank()
                        roundBanked = object.bank()
                        print(f'You banked {score} points in round {counter}')
                        print(f'Total score is {banked} points')
                    elif bank == 'q':
                        print(f'Total score is {banked} points')
                        print(f'Thanks for playing. You earned {banked} points')
                        break
                elif decide == 'q' and counter > 1:
                   print(f'Total score is {banked} points')
                   print(f'Thanks for playing. You earned {banked} points')
                   break
                else:
                    print(f'Thanks for playing. You earned {banked} points')
                    break
                counter +=1





if __name__ == '__main__':
    cal = 5
    game =Game(GameLogic.roll_dice)
    game.play()