# for 循环一般都是一个有区间的循环，类似于一个迭代器的作用。

example_list = [1, 2, 3, 4, 5, 6] # 定义一个可供for迭代的list列表

for i in example_list: # 进行example_list列表中元素的迭代
    print(i) # 输出从example_list列表中迭代出来的每个元素

# python里有一个针对for循环遍历迭代器比较有用的函数：range()
# range函数可以生成连续的可供迭代的一个自然数列表，可以充当迭代器的index索引
# range(1, 5)生成的是[1, 2, 3, 4], 从1到5，递增且步长为1的自然数列表，所以range的参数区间是‘前包后不包’的
# range(1, 5, 2)生成的是[1, 3], 从1到5，递增且步长为2的自然数列表
for i in range(1, 5):
    print(i)
    print(example_list[i]) # i相当于example_list列表的index索引，来获取对应索引的元素值