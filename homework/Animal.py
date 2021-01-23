class Animal:
    # name = "name"
    # colour = "colour"
    age = "1"
    # gender = "gender"
    def __init__(self):
        self.name = 'Cross'
        self.colour = "white"
        self.gender = "female"

    def cry(self):
        self.loud = "woof"
        print(f"这只大的动物这样叫{self.loud}")

    def run(self):
        print("父类会跑的方法")


if __name__ == '__main__':
    big_animal = Animal()
    small_animal = Animal()
    # print(small_animal.name)
    big_animal.cry()
    # print(small_animal.name,small_animal.cry())

    #通过类改属性
    print(big_animal.age)
    Animal.age = "3"
    print(big_animal.age)

