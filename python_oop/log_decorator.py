import logging
#设置基本配置
logging.basicConfig(level=logging.INFO)
#自定义logger
logger = logging.getLogger('log')

#定义一个装饰器
#ba把函数当成参数传进来，在定义一个函数,接受任何形式的参数，不管func里面传什么
def log_decorator(func):
    """
    给传入的函数增加日志信息
    :param func:传入的参数
    :return:添加了log信息的日志
    """
    def wrapper(*args,**kwargs):
        #加上log信息
        logger.info(f"装饰器：{log_decorator.__name__}->传入函数：{func}")
        #调用传入的函数对象
        return func(*args,**kwargs):


