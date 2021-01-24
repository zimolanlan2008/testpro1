import money
# from money import saved_money
# salary = 1000

def send_money(salary):
    print(f"发工资前的存款：{money.saved_money}")
    money.saved_money += salary
    print(f"发工资后的存款：{money.saved_money}")
    return money.saved_money