"""
自己完成比较烂，最后看了别人代码后写的
原有存款 1000元， 发工资之后存款变为2000元
定义模块
1、money.py saved_money = 1000
2、定义发工资模块 send_money，用来增加收入计算
3、定义工资查询模块 select_money，用来展示工资数额
4、定义一个start.py ，启动文件展示最终存款金额
5、如果循环发送工资n次，查询第N次发的工资以及存款情况
6、如果薪资每月涨200，怎么弄？,这个工资循环是应该放在哪里？启动项？还是单独定义一个模块？
"""

saved_money = 1000


# 2、定义发工资模块 send_money，用来增加收入计算
def send_money(salary):
    global saved_money
    print(f"发工资前存款:{saved_money}")
    saved_money += salary
    print(f"发工资后存款:{saved_money}")

    return saved_money


def select_money(salary):
    # for i in range(10):
    #     salary = salary+200*i
    print(f"当前工资为：{salary}")
    return salary


if __name__ == '__main__':
    # salary = 2000
    # select_money(salary)
    # send_money(salary)
    for i in range(10):
        # 为了格式好看点打了空行
        print("")
        print(f"第{i + 1}次工资发送情况")

        salary = 2000
        salary = salary + 200 * i
        send_money(select_money(salary))

        # send_money.send_money(select_money.select_money(2000))
