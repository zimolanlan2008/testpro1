from homework.Animal import Animal

class Cat(Animal):
    #增加一个属性和方法
    #重写父类init,但是要用父类的属性方法，super
    def __init__(self):
        super().__init__()
        self.hair = "short_hair"
        self.gender = "male"

    def catch(self):
        print("捕捉老鼠小能手")

    #重写父类方法
    def cry(self,friend):
        self.loud = "miaow"
        self.friend = friend
        print(f"这只聪明的猫猫这样叫{self.loud},他有一个好朋友叫{self.friend}")

if __name__ == '__main__':
    clever_cat = Cat()
    #传参给朋友名字或者输入一个参数
    clever_cat.cry(input())
    clever_cat.run()
    clever_cat.catch()
    print("这只猫的头发是",clever_cat.hair)
    #调用父类属性
    print(clever_cat.name)
    # 改父类属性值在方法中
    print(clever_cat.gender)
    #可以改父类属性值
    Cat.age = '5'
    print(clever_cat.age)
