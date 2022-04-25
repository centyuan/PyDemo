import random
def main():
    #list表达式
    '''
    [out_exp_res for out_exp in input_list]
    [out_exp_res for out_exp in input_list if condition]
        '''
    names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
    new_names = [name.upper() for name in names if len(name)>3]

    print(new_names)
    #dict表达式
    """
    {key_expr: value_expr for value in collection}
    {key_expr: value_expr for value in collection if condition}
    """
    listdemo = ['Google', 'Runoob', 'Taobao']
    newdict = {key:len(key) for key in listdemo}
    print("_______",newdict)
    #集合推导式
    """
    { expression for item in Sequence }
    { expression for item in Sequence if conditional }
    """
    a = {x for x in 'abracadabra' if x not in 'abc'}
    print(a)
    """
    生成器表达式来初始化元组、数组或其他序列类型
    """
    #元组推导式
    """
    (expression for item in Sequence )
    (expression for item in Sequence if conditional )
    """
    #*是不定长参数，导入tuple
    #**是     导入dict
    #py3.8之后强制位置参数
def printinfo(args,*vartuple,**vardict):
        print('必须参数',args,end='')
        print('不定长参数tuple',vartuple)
        print('不定长参数',vardict)


if __name__ == '__main__':
    main()
    print(random.random())
    print(f"abc{random.random()}")
    print("我叫%s今年%d岁"%('cent',10))
    num = 12 #int(input("输入一个数字："))
    if num % 2 == 0:
        if num % 3 == 0:
            print("你输入的数字可以整除 2 和 3")
        else:
            print("你输入的数字可以整除 2，但不能整除 3")
    else:
        if num % 3 == 0:
            print("你输入的数字可以整除 3，但不能整除 2")
        elif True:
            print('elif条件')
        else:
            print("你输入的数字不能整除 2 和 3")
    printinfo(20,30,40,a=1,b=2)
    import sys
    print(sys.path)
    #使用生成器表达式计算笛卡尔积
    colors = ['black','white']
    sizes = ['S','M','L']
    for Tshirt in ('%s %s'%(c,s) for c in colors for s in sizes):
        printinfo(Tshirt)
    Firewall_data = [
        {"name":'Y',"type":'FireWall',"create_time":"2022-09-10"},
        {"name": 'B', "type": 'FireWall', "create_time": "2022-09-11"},
        {"name": 'A', "type": 'FireWall', "create_time": "2022-09-12"},
        {"name": 'D', "type": 'FireWall', "create_time": "2022-09-13"},
                     ]
    result = [
        {"name": item.get("name"), "type": 'FireWall', "create_time": item.get("create_time")} for item in Firewall_data
    ]
    # for item in Firewall_data:
    #     print(item.get("name"))
    print("+++++++++",type(result),result)