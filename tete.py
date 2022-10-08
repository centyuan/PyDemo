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
e = dict({'three': 3, 'one': 1})
print(e)
print(len(e))

day = range(6)
print(type(day))
course_datas = {'1': 1, '2': 12}

for key,value in course_datas.items():
    print(key,value)

dd = '2022-10-01 23:59'
from datetime import datetime
print(datetime.strptime(dd,"%Y-%m-%d %H:%M"))
dd = [
    {'start_time': '2022-10-01 23:59','end_time': '2022-10-02 12:20'},
    {'start_time': '2022-10-02 11:59','end_time': '2022-10-03'},
    {'start_time': '2022-10-03 23:59','end_time': '2022-10-04'}
]
time_tuple = [(item.get('start_time'), item.get('end_time')) for item in dd]
print(time_tuple)
new_time_tuple = sorted(time_tuple, key=lambda x: x[0])
print('aaaa',new_time_tuple)
for i in range(len(new_time_tuple)):
    if i ==len(new_time_tuple)-1:
        break
    if new_time_tuple[i+1][0]<new_time_tuple[i][1]:
        print('交集')
    else:
        print('没有')