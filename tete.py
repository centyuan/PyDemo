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
# engine.runAndWait()
# import re
# import base64

# import requests
# url_ = "http://192.168.8.34/group1/M00/00/05/wKgIImLQ3feAXhf9AEDLLFxGssA073.mp4?token=d6ce15460d2db26094c8be17a9df8317&ts=1660641493"
# get_web = requests.get(url_)
# with open('web_file','wb+') as f:
#     f.write(get_web.content)