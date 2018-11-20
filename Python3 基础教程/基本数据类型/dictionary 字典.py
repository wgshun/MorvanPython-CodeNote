# python中的字典是一个无序的，以键值对的形式存在的数据类型

# 定义一个字典,字典的键值没有具体规定的数据类型
dict = {'a': 1, 'b': 2}
print(dict)

# 获取字典键为a的值
print(dict['a'])

# 删除键为b的元素
del dict['b']
print(dict)

# 向字典中添加元素
dict['d'] = 3
dict['list'] = [1, 2, 3]
dict['dict'] = {'a':1, 'b':2}
print(dict)

# 获取字典中的字典和列表的对应值
print(dict['list'][2])
print(dict['dict']['b'])