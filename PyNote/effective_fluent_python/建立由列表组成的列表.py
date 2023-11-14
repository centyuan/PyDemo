"""
如果列表里的元素是对其他可变对象的引用的
my_list = [[]] * 3
这种初始化列表，里面三个元素其实是三个引用，而且这三个引用指向同一列表

"""
#1.
borad = [['item'] * 3 for i in range(3)]
#[['item', 'item', 'item'], ['item', 'item', 'item'], ['item', 'item', 'item']]
borad[1][2] = 'Y'
#[['item', 'item', 'item'], ['item', 'item', 'Y'], ['item', 'item', 'item']]

#2.错误的方法,三个引用
weird_board = [['item'] * 3] * 3
#[['item', 'item', 'item'], ['item', 'item', 'item'], ['item', 'item', 'item']]
weird_board[1][2] = 'M'
#[['item', 'item', 'M'], ['item', 'item', 'M'], ['item', 'item', 'M']]

#3.错误的方法,也是三个引用
row =['item'] *3
board =[]
for i in range(3):
    borad.append(row) #追加同一个对象（row）3 次

#4.正确的方法
board = []
for i in range(3):
    #每次迭代中都新建了一个列表，追加到board中
    row =['item'] *3
    borad.append(row)

