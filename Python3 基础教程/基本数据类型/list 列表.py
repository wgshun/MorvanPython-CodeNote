# 介绍python中list列表的相关操作
# list是有序可重复的数据类型

# 定义一个list列表
a = [1, 2, 3, 3, 2, 1]
print('init:', a)

# 使用append向已知列表中添加元素
a.append(4) # 在列表末尾追加
print('added:', a)

# 使用insert向已知列表中插入元素
a.insert(1, 0) # 在列表索引为1的位置插入元素0
print('inserted:', a)

# 使用remove在已知列表中删除元素
a.remove(1) # remove函数的参数是要删除的元素值，并非元素的索引，有多个相同值元素时只删除第一个为该值的元素
print(a)

# 使用索引获取list中对应的元素值
print(a[-1]) # 获取最后一个元素的值
print(a[1]) # 获取第二个元素的值
print(a[1:3]) # 获取第二个和第三个元素的值
print(a[:3]) # 获取前三个元素的值
print(a[3:]) # 获取第四个往后所有的元素的值
print(a[-3:]) # 获取最后三个元素的值

# 使用index获取列表中第一次出现指定元素值的索引
print(a.index(2))

# 使用count计算列表中出现指定元素的数量
print(a.count(3))

# 使用sort对列表中的元素从小到大排序
a.sort()
print(a)
a.sort(reverse=True) # 使用sort函数的reverse参数对列表中的元素从大到小排序
print(a)