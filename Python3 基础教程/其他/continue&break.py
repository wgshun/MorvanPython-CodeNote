# 前面说到循环语句和判断语句，在语句执行过程中可以使用continue和break进行跳过和终止操作

# continue跳过当前循环操作
a = True # 定义一个变量为True
while a: # 循环条件就是当a = True时
    b = input('Give a number:') # 输入一个数字
    if b == '6': # 当数字为6时，
        # a = False # 使变量a = False，下次循环时不满足循环条件，循环既结束，此种情况会输出本次循环最后的提示
        # break # 使用break即可直接终止此循环，此种情况不会输出本次循环最后的提示
        continue # 使用continue即可直接跳过本次循环，此种情况不会输出本次循环最后的提示
    else: # 当数字不为6时，
        pass # pass继续向下执行
    print('Still in while.') # 在每个循环的最后输出一个提示

print('Out.')# 输出循环结束的提示