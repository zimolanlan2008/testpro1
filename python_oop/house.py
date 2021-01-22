"""
class 类名:
    多个类属性。。。
    多个类方法。。。
类名：有代表功能性
多个单词，首字母大写，驼峰
看看房子有什么属性，能完成哪些功能
门、地板就是静态属性
睡觉吃饭时动态属性方法
把图纸变成真实房子，就是实例化
"""

class House:
    #静态属性
    door = 'red'
    floor = "white"
    #构造方法，在类实例化的时候自动执行
    def __init__(self):
        #加上self.就变成了实例变量
        print(self.floor)
        #定义实例变量,类之中，方法之类，必须以self.变量名方式定义
        #实例变量的作用域是整个类中的所有方法，扩大作用域
        self.kitchen = "cook"
    #动态方法
    def sleep(self):
        #普通变量->在类之中，方法之中，并且没有self
        self.bed = "萌死"
        print(f"在房子里面可以在{self.bed}睡觉")
    def cook(self):
        print("在房子里面可以做饭")

if __name__ == '__main__':
    #实例化->变量 =类（）
    north_house = House()
    china_house = House()

    #看看能不能调用到类的方法
    #通过实例对象调用类属性
    print(north_house.door)

    #通过类直接修改属性
    House.door = "green"

    print(north_house.door)

    #通过实例修改属性,只影响实例变化，不影响类里面属性值
    north_house.floor = "brown"
    print(north_house.floor)
    print(House.floor)

