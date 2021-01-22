#继承Game
from python_oop.game_oop import Game

class HouYi(Game):
    def __init__(self):
        self.defense = 100
        #继承父类构造方法
        super().__init__()
    def fight(self):
        #改造一下my _hpj计算方式






if __name__ == '__main__':
    houyi = HouYi()
    print(houyi.my_hp)