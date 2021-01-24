import select_money
import send_money

if __name__ == '__main__':
    # salary = 2000
    # send_money(salary)
    # select_money(salary)
    # select_money.select_money()
    # print(select_money.select_money())
    # send_money(1000)
    # send_money.send_money(select_money.select_money(2000))

    for i in range(10):
        print("")
        print(f"第{i+1}次工资发送情况")
        send_money.send_money(select_money.select_money(2000))
