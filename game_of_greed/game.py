from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker
import collections

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
        self.roller = roller or GameLogic.roll_dice
    def play(self):
        counter = 1
        print('Welcome to Game of Greed')
        wanna_play=(input('Wanna play? '))
        if (wanna_play =='n'):
            print('OK. Maybe another time')
        else:
            object = Banker()
            banked = 0
            beaking = True
            while beaking and counter <= 10:
                roundBanked = 0
                print(f'Starting round {counter}')
                shelf = 0
                roll = 6

                def func(counter,banked, shelf, roll):
                    print(f'Rolling {roll} dice...')
                    roll_dice = self.roller(roll)
                    nums=[]
                    for i in roll_dice:
                        nums.append(str(i))
                    tuple_nums = tuple(int(i) for i in nums) 

                    expected_score = GameLogic.calculate_score(tuple_nums)
                    print(','.join(nums))
                    if expected_score == 0 :
                        print('Zilch!!! Round over')
                        print(f'You banked 0 points in round {counter}')
                        print(f'Total score is {banked} points')
                        return True
                    decide = input('Enter dice to keep (no spaces), or (q)uit: ')
                    score = 0
                    if decide != 'q':
                        var = tuple(int(i) for i in decide) 
                        int_decide = tuple(int(i) for i in decide)
                        length = 6 -len(var)
                        variable= ''.join(sorted(nums))
                        counter_decide = list(int_decide)
                        counter_nums = list(tuple_nums)
                        def cheater():
                            print('Cheater!!! Or possibly made a typo...')
                            print(','.join(nums))
                            decide = input('Enter dice to keep (no spaces), or (q)uit: ')
                            var = tuple(int(i) for i in decide) 
                            score = GameLogic.calculate_score(var)
                            length = 6 -len(var)
                        try:
                            for i in counter_decide:
                                counter_nums.remove(i)
                        except:
                            raise cheater()

                        score = GameLogic.calculate_score(var)
                        shelf = object.shelf(score)
                        roll -=len(var)
                        print(f'You have {shelf} unbanked points and {roll} dice remaining')
                        bank = input('(r)oll again, (b)ank your points or (q)uit ')
                        if bank == 'b':
                            # object = Banker()
                            banked = object.bank()
                            roundBanked = object.bank()
                            print(f'You banked {shelf} points in round {counter}')
                            print(f'Total score is {banked} points')
                        elif bank == 'q':
                            print(f'Total score is {banked} points')
                            print(f'Thanks for playing. You earned {banked} points')
                            beaking = False
                            return beaking
                        elif bank =="r":
                            if func(counter,banked,shelf,roll) == False:
                                beaking =False
                                return beaking
                            beaking = True
                            return beaking
                        return True
                    elif decide == 'q' and counter > 1:
                         print(f'Total score is {banked} points')
                         print(f'Thanks for playing. You earned {banked} points')
                         beaking = False
                         return beaking
                    else:
                        print(f'Thanks for playing. You earned {banked} points')
                        beaking = False
                        return beaking
                beaking = func(counter,banked,shelf, roll)
                counter +=1





if __name__ == '__main__':
    cal = 5
    game =Game(GameLogic.roll_dice)
    game.play()