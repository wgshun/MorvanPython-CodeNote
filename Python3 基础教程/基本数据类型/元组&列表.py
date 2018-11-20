# tuple(元组)和list(列表)都是python 中的数据类型，都是可迭代的数据类型
# 两者不同的是元组的元素不可修改

# 定义元组的两种方式
a_tuple = (1, 11, 12, 13, 14)
b_tuple = 1, 3, 5, 7, 9

# 定义列表的方式
a_list = [1, 2, 3, 4, 5]

# 通过for循环迭代元组和列表中的元素
for i in a_tuple: # 以整个元组作为迭代器
    print(i)

for i in a_list: # 以整个列表作为迭代器
    print(i)

for ind in range(len(a_list)): # 以列表或元组的length长度作为迭代器
    print('index =', ind, ', number =', a_list[ind]) # a_list[*]根据列表的索引输出指定的元素