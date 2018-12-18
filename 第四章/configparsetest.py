import configparser

config = configparser.ConfigParser()
config.read('i.cfg',encoding='UTF-8')

# 获取section
secs = config.sections()
print(secs)

# 获取section的keys
# options = config.options('group2')
# print(options)

# 获取section的键值对内容
# item_list = config.items('group2')
# print(item_list)

# 获取某个option的内容
# val = config.get('group1','k1')
# val2 = config.getint('group1','k2')
# print(val)
# print(val2)

# 删除某个section
# sec = config.remove_section('group1')
# config.write(open('i.cfg',"w"))

# 添加一个section
# sec = config.has_section('wupeiqi')
# sec = config.add_section('wupeiqi')
# config.write(open('i.cfg', "w"))

# config.set('group2','k1','1111')
# config.write(open('i.cfg', "w"))

# 删除某个section
# config.remove_option('group2','age')
# config.write(open('i.cfg', "w"))
