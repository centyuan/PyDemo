# import turtle
# import time
#
# turtle.pensize(10)
# turtle.pencolor("blue")
#
# # P
# turtle.left(90)
# turtle.fd(100)
# turtle.right(90)
# turtle.forward(20)
# turtle.circle(-26, 180)
# turtle.forward(20)
# # Y
# turtle.penup()
# turtle.goto(80, 100)
# turtle.pendown()
# turtle.seth(-90)
# turtle.fd(30)
# turtle.circle(25, 90)
# turtle.fd(15)
# turtle.penup()
# turtle.goto(125, 100)
# turtle.seth(-90)
# turtle.pendown()
# turtle.fd(80)
# turtle.circle(-20, 90)
# turtle.fd(20)
# # t
# turtle.penup()
# turtle.goto(155, 100)
# turtle.pendown()
# turtle.seth(0)
# turtle.fd(40)
# turtle.penup()
# turtle.goto(175, 120)
# turtle.seth(-90)
# turtle.pendown()
# turtle.fd(60)
# turtle.circle(20, 90)
# # h
# turtle.penup()
# turtle.goto(230, 140)
# turtle.seth(-90)
# turtle.pendown()
# turtle.fd(100)
# turtle.bk(55)
# turtle.left(90)
# turtle.fd(25)
# turtle.circle(-15, 90)
# turtle.fd(40)
# # o
# turtle.penup()
# turtle.goto(295, 73)
# turtle.seth(90)
# turtle.pendown()
# turtle.circle(-28)
# # n
# turtle.penup()
# turtle.goto(375, 100)
# turtle.seth(-90)
# turtle.pendown()
# turtle.fd(60)
# turtle.bk(55)
# turtle.left(90)
# turtle.fd(25)
# turtle.circle(-15, 90)
# turtle.fd(40)
import turtle
import requests
from urllib.parse import quote
import re


# 这个函数就是打印汉字 没有移动的轨迹
def writeWord(target_word, startx, starty):  # 基于坐标，打印汉字
    """
    基于坐标，打印单个汉字
    :param target_word: 目标汉字
    :param startx: 起始位置x
    :param starty: 起始位置y
    :return:
    """
    turtle.color("black", "black")  # 设置画笔颜色
    turtle.pu()  # 抬起画笔
    turtle.goto(startx, starty)  # 移动到指定位置
    turtle.pd()  # 下笔
    turtle.write(target_word, move=False, align='left', font=('汉仪程行简', 120, 'normal'))  # 打印汉字

# 这个函数是爬虫获取汉字的笔画坐标信息
def obtain_coordinate(target_word):  # 获取汉字的坐标
    """
    获取汉字的坐标
    :param target_word:
    :return:
    """
    url = "https://bihua.bmcx.com/web_system/bmcx_com_www/system/file/bihua/get_0/"

    params = {
        'font': quote(target_word).replace("%", "").lower(),
        'shi_fou_zi_dong': '1',
        'cache_sjs1': '20031914',
    }
    response = requests.get(url, params=params)
    content = response.text
    content = content.replace('hzbh.main(', '').split(');document.getElementById')[0]
    content = content.split('{')[-1].split("}")[0]
    pattern = re.compile(r'\w:\[(.+?)\]')
    result = re.split(pattern, content)
    order_xy_routine = []
    words_cnt = 0
    for r in result:
        sec = re.findall(r'\'.+?\'', r)
        if len(sec):
            orders = sec[1].split('#')
            for order in orders:
                order_str = re.findall(r'\(\d+,\d+\)', order)
                order_xy = [eval(xy) for xy in order_str]
                order_xy_routine.append(order_xy)
            words_cnt += 1
    print(order_xy_routine)
    return order_xy_routine


#这个函数是根据汉字的笔画坐标信息，打印汉字 有笔画的轨迹
def draw_words(target_words, startx, starty, lineNum=1):  # 画汉字
    """
    画汉字
    :param target_words:
    :param startx:
    :param starty:
    :param lineNum:
    :return:
    """
    turtle.color("black", "black")  # 设置画笔颜色
    turtle.pu()  # 抬起画笔
    coordinates = obtain_coordinate(target_words)
    for index, coordinate in enumerate(coordinates):
        turtle.goto((startx + coordinate[0][0])/2, -(starty + coordinate[0][1])/2)
        turtle.pd()
        for xy in coordinate:
            x,y=xy
            turtle.goto((startx+x)/2, -(starty+y)/2)
        turtle.pu()



if __name__ == '__main__':
    # 方法一  直接打印汉字
    # writeWord("彩虹", -120, -60)

    # 方法二  画汉字
    draw_words("文", -200, 0)
    draw_words("狗", 0, 0)


    turtle.done()  # 保证界面不退出 可点击右上角关闭
