import collections
import random


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

class GameLogic:

    @staticmethod
    def calculate_score(tuple:tuple):
        score=0
        count=collections.Counter(tuple).most_common()
        sort= sorted(tuple)

        print(count)
        for i in count:
            score += rules[i]
        return score

    