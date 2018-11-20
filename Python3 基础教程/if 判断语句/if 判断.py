# 定义自变量并赋值
a, b, c = 1, 2, 3

if a < b < c: # 判断a是否小于b，b同时也小于c，如果判断成立则执行if里面的代码，否则不执行
    print('a is less than b and b is less than c.')

x, y, z = 1, 2, 0
if x < y > z: # 判断x是否小于y，z同时也小于y，如果判断成立则执行if里面的代码，否则不执行
    print('x is less than y and z is less than y.')
if x!=y: # 判断x是否不等于y，如果判断成立则执行if里面的代码，否则不执行
    print('x is not equal to y.')

e, f = 1, 1
if e <= f: # 判断e是否小于或等于f，如果判断成立则执行if里面的代码，否则不执行
    print('e is less or equal to f.')
if e==f: # 判断e是否等于f，如果判断成立则执行if里面的代码，否则不执行
    print('e is equal to f.')
