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
# ssr_info = "cn01.efan.men:8751:origin:rc4-md5:http_post:ZWZhbmNjeXVu/?obfsparam=NjU0NTQtMEd5NGdiMFBlMi5kb3dubG9hZC5taWNyb3NvZnQuY29t&protoparam=&remarks=6aaZ5rivMDE&group=6aW_6aWtY2PkupEgLSBH6K6h5YiS77yIMTAwMEdC77yJ&udpport=0&uot=0"
# ssr_data = re.match("(.*)\&group", ssr_info).group(1)
# print(ssr_data)
# ssr_data = ssr_data.encode()
# ssr_data = base64.b64encode(ssr_data).decode()
# print(ssr_data)
#
# import base64
#
# str = "i love qiqi".encode()
# # 对字符串进行编码
# bs4str = base64.b64encode(str)
# # 输出编码后的字符串
# print('1:',bs4str,bs4str.decode())
# # 输出还原编码后的字符串
# print('2:',base64.b64decode(bs4str))
#
# str = "https://www.baidu.com".encode("utf-8")
# # 对url进行编码
# urlstr = base64.urlsafe_b64encode(str)
# # 输出url编码后的字符串
# print('3:',urlstr)
# # 还原编码后的字符串
# print('4:',base64.urlsafe_b64decode(urlstr))
# # 运行结果
# # b'aSBsb3ZlIHFpcWk='
# # b'i love qiqi'
# # b'aHR0cHM6Ly93d3cuYmFpZHUuY29t'
# # b'https://www.baidu.com'
