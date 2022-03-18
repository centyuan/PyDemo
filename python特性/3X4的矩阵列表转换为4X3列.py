# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/2/26 22:04

def main():
    matrix = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]
    ]
    # 嵌套列表解析
    new_matrix = [[row[i] for row in matrix] for i in range(len(matrix)+1)]
    new_matrix = [[row[i] for row in matrix] for i in range(len(matrix)+1)]
    print(new_matrix)


if __name__ == '__main__':
    main()