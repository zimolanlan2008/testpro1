class Game:
    # def __init__(self):
    #     #初始化属性
    # self.my_hp = 1000
    # self.my_power = 200
    # self.enemy_hp = 1000
    # self.enemy_power = 199
    def __init__(self,my_hp,enemy_hp,):
        #初始化属性
    self.my_hp = 1000
    self.my_power = 200
    self.enemy_hp = 1000
    self.enemy_power = 199

    #定义个对打方法
    def fight(self):
        while True:
            #我的剩余血量
            self.my_hp =self.my_hp - self.enemy_power
            #
            self.enemy_hp -= self.enemy_power
            if self.my_hp <= 0:
                print("我输了")
                break
            elif self.enemy_hp <= 0:
                print("我赢了")
                break


if __name__ == '__main__':
    game = Game()
    game.fight()