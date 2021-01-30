"""
补全计算器中加法和除法的测试用例
使用参数化完成测试用例的自动生成
在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】
"""

# 计算器测试代码
import pytest
import yaml

from python_code.calc import Calculator

with open('./datas/calc.yaml') as f:
    datas = yaml.safe_load(f)
    adddatas = datas['add']
    adddatas_data = adddatas['datas']
    myid_add = adddatas['myid']
    # adddatas = yaml.safe_load(f)['add']
    # # divdatas = yaml.safe_load(f)['div']
    # datas1 = adddatas['datas']
    # myid1 = adddatas['myid']
    # datas2 = divdatas['datas']
    # myid2 = divdatas['myid']

    # print(datas2, myid2)
    divdatas = datas['div']
    divdatas_data = divdatas['datas']
    myid_div = divdatas['myid']


class TestCalc:
    def setup(self):
        print("开始计算")
        self.clac = Calculator()

    def teardown(self):
        print("计算结束")

    @pytest.mark.parametrize("a,b,expect", adddatas_data,
                             ids=myid_add)
    def test_add(self, a, b, expect):
        # 实例化计算机类
        # clac = Calculator()
        if isinstance(a, str):
            print("非数字类型")
            assert False

        elif a is None:
            print("不能为空")
            assert False

        elif 999999 <= a or a <= -999999:
            print("超出最大值")
            assert False

        else:
            # 调用类Calculator里面的add方法
            result = self.clac.add(a, b)
            # 浮点数的判断
            if isinstance(result, float):
                result = round(result, 2)
            # 得到结果之后验证
            assert result == expect


    @pytest.mark.parametrize("a,b,expect", divdatas_data, ids=myid_div)
    def test_div(self, a, b, expect):
        # 判断b不能等于0
        if b == 0:
            print("除数不能等于0")
            assert False

        elif a is None:
            print("不能为空")
            assert False

        elif 999999 <= a or a <= -999999:
            print("不能低于最小值")
            assert False


        else:
            result = self.clac.div(a, b)
            if isinstance(result, float):
                result = round(result, 2)

            assert result == expect

# def test_add1(self):
#     # 实例化计算机类
#     # clac = Calculator()
#     # 调用类Calculator里面的add方法
#     result = self.clac.add(0.1, 0.1)
#     # 得到结果之后验证
#     assert result == 0.2
#     print(result)
#
# def test_add2(self):
#     # 实例化计算机类
#     # clac = Calculator()
#     # 调用类Calculator里面的add方法
#     result = self.clac.add(-1, -1)
#     # 得到结果之后验证
#     assert result == -2
#     print(result)
#
# def test_add3(self):
#     # 实例化计算机类
#     # clac = Calculator()
#     # 调用类Calculator里面的add方法
#     result = self.clac.add(99, 101)
#     # 得到结果之后验证
#     assert result == 2
#     print(result)
