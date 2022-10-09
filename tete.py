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
import requests
import cv2
def get_duration_from_cv2(filename):
  cap = cv2.VideoCapture(filename)
  if cap.isOpened():
    rate = cap.get(5)
    frame_num =cap.get(7)
    duration = frame_num/rate
    return int(duration)
  return 0

url = "http://rihlu8ghc.bkt.clouddn.com/courseware/%E8%A3%B8%E8%81%8A587296aa2478411ed9ae7000c29d2d2c0.mp4?sign=c617909575108da81e45461ff991038e&t=63425ffe"
result = get_duration_from_cv2(url)
print(result)
url_ = "http://192.168.8.242:9000/api/teacher/login"
to_data = {
  "username":"teacher12",
  "password":"123456"
}
new_h = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
}
res = requests.post(url,headers=new_h,json=to_data)
print('返回')
print(res.json(),res.headers)