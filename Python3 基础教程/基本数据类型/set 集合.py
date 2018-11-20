# python中的集合是无序不重复的数据类型

# 创建一个集合的两种方式
set_1 = set('abcda')
set_2 = {'a', 'b', 'c', 'a'}
# 创建一个空集合必须用set()而不是{ }，因为{ }是用来创建一个空字典

print(set_1)  # 输出集合，重复的元素被自动去掉

# set可以进行集合运算
a = set('abcdef')
b = set('aefghi')

print(a)

print(a - b)  # a 和 b 的差集

print(a | b)  # a 和 b 的并集

print(a & b)  # a 和 b 的交集

print(a ^ b)  # a 和 b 中不同时存在的元素