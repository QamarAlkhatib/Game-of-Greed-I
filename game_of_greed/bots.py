"""Place in root of Game of Greed Project,
at same level as pyproject.toml
"""

import builtins
import re
from abc import abstractmethod
import collections
import re
from game_of_greed.game import Game
from game_of_greed.game_logic import GameLogic


class BasePlayer:
    def __init__(self):
        self.old_print = print
        self.old_input = input
        builtins.print = self._mock_print # Methods overriding
        builtins.input = self._mock_input # Methods overriding
        self.total_score = 0

    def reset(self):
        builtins.print = self.old_print
        builtins.input = self.old_input

    # The default behaviour
    @abstractmethod
    def _mock_print(self, *args):
        self.old_print(*args)

    @abstractmethod
    def _mock_input(self, *args):
        return self.old_input(*args)

    @classmethod
    def play(cls, num_games=1):

        mega_total = 0

        for i in range(num_games):
            player = cls()
            game = Game() # doesn't pass a mock roller
            try:
                game.play()
            except SystemExit:
                # in game system exit is fine
                # because that's how they quit.
                pass

            mega_total += player.total_score
            player.reset()

        print(
            f"Congrats! {num_games} games (maybe) played with average score of {mega_total // num_games}"
        )


class Group2Bot(BasePlayer):

    def _mock_print(self, *args):
        self.old_print(*args)
        printed_data = str(args[0])
        if printed_data[0].isdigit():
            self.rolled_dice = tuple(int(ch) for ch in printed_data.split(','))
        
        if printed_data[0] == "Y" and printed_data[1] == "o":

            self.remained_dice = re.findall(r'and (.*?) dice', printed_data)


    def _mock_input(self, *args):
        self.old_print(*args)
        if args[0].startswith('Wanna play'):
            return 'y'

        elif args[0].startswith('Enter dice'):
            dice = list(self.rolled_dice)
            dice_chosing = ""
            

            if sorted(dice) == [1,2,3,4,5,6] or (collections.Counter(dice).most_common(1)[0][1] == 2 and len(collections.Counter(dice).most_common()) == 3):
                # print("".join(str(i) for i in dice))
                return "".join(str(i) for i in dice)
            
            else:
                if 1 in sorted(dice) or 5 in sorted(dice):
                    count_1=dice.count(1)
                    count_5=dice.count(5)
                    if count_1 != 0 and count_5 != 0:
                        all_count = count_1*"1" + count_5*"5"
                        dice_chosing += all_count

                    elif count_1 != 0:
                        dice_chosing += count_1*"1"
                    elif count_5 != 0 :
                        dice_chosing += count_5*"5"

                if dice.count(2) > 2 :
                    count_2 = dice.count(2) * "2"
                    dice_chosing += count_2

                if dice.count(3) > 2 :
                    count_3 = dice.count(3) * "3"
                    dice_chosing += count_3

                if dice.count(4) > 2 :
                    count_4 = dice.count(4) * "4"
                    dice_chosing += count_4

                if dice.count(6) > 2 :
                    count_6 = dice.count(6) * "6"
                    dice_chosing += count_6
                # print(dice_chosing)
                return dice_chosing   

        elif args[0].startswith('(r)oll again,'):
            dice = int(self.remained_dice[0])
            # print("******************the dice : ",self.remained_dice[0])
            if dice > 2 :
                return "r"
            else:
                return "b"




        elif True:
            pass
        
        elif args[0].startswith('(r)oll again, (b)ank your points or (q)ui'):
            return 'b'
        else:
            return 'q'

if __name__=="__main__":
    # bot1 = BasePlayer()
    # bot1.play()
    amman_bot = Group2Bot()
    amman_bot.play()