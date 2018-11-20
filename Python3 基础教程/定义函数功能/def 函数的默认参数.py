# 首先定义一个函数
def sale_car(price, colour='red', is_second_hand=False): # colour和is_second_hand这两个参数在定义的时候给了它们默认的值
    print('price:', price,
          'colour:', colour,
          'is_second_hand:', is_second_hand)

# 调用函数
sale_car(10000) # 该函数有三个参数，有两个参数是有默认值的，所以只需要给一个参数就可以了
sale_car(22222, colour='blue') # 想改变默认参数的值就需要在调用函数的时候指定需要更改的参数
