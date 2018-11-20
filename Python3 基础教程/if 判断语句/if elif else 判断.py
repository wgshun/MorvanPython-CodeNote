# if...elif...else... 是多重判断语句，其中的elif...可以根据需要往上加（可以重复添加）
# 定义自变量并赋值
x = -2

if x > 1: # 判断x是否大于1，如果判断成立则执行if里面的代码，否则跳过
    print('x is greater than 1.')
elif x < 1: # 判断x是否小于1，如果判断成立则执行if里面的代码，否则跳过
    print('x is less than 1.')
elif x < -1: # 判断x是否小于-1，如果判断成立则执行if里面的代码，否则跳过
    print('x is less than -1.')
else:
    print('x is equal to 1.')

# 上述判断中 x = -2, 同时满足第一个和第二个elif，但是在执行的时候python就会执行第一个elif，忽略第二个elif