#_*_coding:utf-8_*_
user_status = False #用户登录了就把这个改成True

def login(auth_type): #把要执行的模块从这里传进来
    def auth(func):
        def inner(*args,**kwargs):#再定义一层函数
                    return func(*args,**kwargs) # 看这里看这里，只要验证通过了，就调用相应功能
            else:
                print("only support qq ")
        return inner #用户调用login时，只会返回inner的内存地址，下次再调用时加上()才会执行inner函数

    return auth

def home():
    print("---首页----")

@login('qq')
def america():
    #login() #执行前加上验证
    print("----欧美专区----")

def japan():
    print("----日韩专区----")

@login('qq')
def henan(style):
    '''
    :param style: 喜欢看什么类型的，就传进来
    :return:
    '''
    #login() #执行前加上验证
    print("----河南专区----")


henan("33333")