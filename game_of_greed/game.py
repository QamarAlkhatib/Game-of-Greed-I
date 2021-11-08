
class Game():
    def __init__(self,roller=None):
        self.roller = roller

    def play(self):
        print('Welcome to Game of Greed')
        wanna_play=(input('Wanna play? '))
        print('OK. Maybe another time')