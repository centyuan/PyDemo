# import pyttsx3
#
# engine = pyttsx3.init()  # 创建对象
# rate = engine.getProperty('rate')  # 获取当前语速
# engine.setProperty('rate', 125)  # 重设语速
# volume = engine.getProperty('volume')  # 获取当前音量(最小为0，最大为1)
# engine.setProperty('volume',1.0)  # 在0-1之间
# voices = engine.getProperty('voices')  # 获取当前发音的详细信息
#
# engine.say('有志者，事竟成，破釜沉舟，百二秦关终属楚；苦心人，天不负，卧薪尝胆，三千越甲可吞吴')
# engine.say(
#     'I love three things in the world ,The sun,the moon and you , the sun for the day, the moon for the night and you forever')
# engine.save_to_file('音频保存为文件', 'audio_file')  # 音频保存为文件
"""
声明全局变量:global
声明非本层的局部变量:nonloacl
查看全局变量:globals()
查看局部变量:locals()
查看变量:vars([object]) # 不传参数相当于locals(),传入对象后或得到object.__dict__

"""
# import time
#
# import requests
# import cv2
# def get_duration_from_cv2(filename):
#   cap = cv2.VideoCapture(filename)
#   if cap.isOpened():
#     rate = cap.get(5)
#     frame_num =cap.get(7)
#     duration = frame_num/rate
#     return int(duration)
#   return 0

# t1 = time.time()
# g = ({x:x}for x in range(50000000))
# for item in g:
#   pass
# t2 = time.time()
# print('g',g,t2-t1)
#
# t3 = time.time()
# g1 = [{x:x}for x in range(50000000)]
# for item in g1:
#   pass
# t4 = time.time()
# print('l',t4-t3)

# https://segmentfault.com/a/1190000020769188?utm_source=tag-newest
# https://blog.fundebug.com/2019/03/07/understand-http2-and-http3/

