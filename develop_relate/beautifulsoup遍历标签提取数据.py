import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import re
import time

def get_importinfo(url):
    """
    :param url 页面路径
    :return  wx_list,qq_list,tg_list,email_list
    """
    try:
        wx_key = ["微信", "wx", "vx", "WX","VX"]
        qq_key = ["QQ", "qq"]
        tg_key = ['TG', '电报', 'telegram']
        email_regex = r"([a-zA-Z0-9_.+-]+@[a-pr-zA-PRZ0-9-]+\.[a-zA-Z0-9-.]+)"
        wx_list, qq_list, tg_list, email_list = [], [], [], []
        options = webdriver.ChromeOptions()
        options.add_argument('headless')  # 无头浏览器
        browser = webdriver.Chrome(
            executable_path=r"D:\python_data\centyuan\cent30\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe",
            options=options)  # 调用带参数的谷歌浏览器
        # browser = webdriver.Chrome(executable_path=r"D:\python_data\centyuan\cent30\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe")  # 调用带参数的谷歌浏览器
        browser.get(url)
        # print('页面动态')
        time.sleep(5)
        # print(browser.page_source)  # 获取动态页面
        ht_str = """
        <body>
        <div>
           </p>
  <p> <strong>E-mail: ComingZOO@gmail.com</strong><br>
                <a href="http://wpa.qq.com/msgrd?V=1&amp;Uin=1277981160&amp;Site=ComingZOO.com全球服飾批發網&amp;Menu=yes" target="_blank"><img src="http://wpa.qq.com/pa?p=1:1277981160:4" height="16" border="0" alt="QQ"> 
    1277981160</a> 
                <a href="http://wpa.qq.com/msgrd?V=1&amp;Uin=763997839&amp;Site=ComingZOO.com全球服飾批發網&amp;Menu=yes" target="_blank"><img src="http://wpa.qq.com/pa?p=1:763997839:4" height="16" border="0" alt="QQ"> 
    763997839</a> 
                    <img src="http://www.okonlineshop.com/logo/line.jpg" width="18" height="18" border="0" alt="LINE">LINE:comingzoo 
                    <img src="http://www.okonlineshop.com/logo/whatsapp.png" width="18" height="18" border="0" alt=" WhatsApp"> 
    WhatsApp:+852 91478002 
                    <img src="http://www.okonlineshop.com/logo/wechat.png" width="18" height="18" border="0" alt="WECHAT"> 
    微信WeChat:comingzoo                        <br>
         </p>
        </div>
        </body>
        """
        ht_page = browser.page_source
        print(ht_page)
        soup = BeautifulSoup(ht_str, 'lxml')
        soup.prettify()
        headers = {
            "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Mobile Safari/537.36",}

        # soup = BeautifulSoup(res.text,'lxml')
        label_list = []
        for child in soup.body.descendants:
            print('++++++++++++')
            # print("chilie.string:", child.string)   # 如果一个节点只包含一个文本节点，或者是只包含一个节点，那么可以使用该属性获取该文本节点的文本内容，
            # print("child.get_text():", child.get_text())  # get_text()方法,这个方法获取到tag中包含的所有文版内容包括子孙tag中的内容
            # print(child.strings)  # .strings 属性来获取其子孙节点的所有文本,返回的是一个迭代器 用for text in child.strings print(text)
            # print(child.stripped_strings) # stripped_strings 和strings属性一样，但会去掉换行和空格
            # https://blog.csdn.net/fengzhen8023/article/details/82903257
            if child.string:
                # print(child.name)
                # print(child)
                print("chilie.string:", child.string)
                label_list.append(child.string)

            else:
                print("child.get_text():", child.get_text())
                label_list.append(child.get_text())
            print("#############")
        label_list = list(set(label_list))
        for label in list(set(label_list)):
            for regex in wx_key:
                if re.findall(regex, label):
                    # print(regex,label)
                    if len(label) < 60:
                        wx_list.append(str(label).strip())
                        break
            for regex in qq_key:
                if re.findall(regex, label):
                    # print("正则:",regex,re.findall(regex, label))
                    if len(label) < 60:
                        qq_list.append(str(label).strip())
                        break
            for regex in tg_key:
                if re.findall(regex, label):
                    # print(regex,label)
                    if len(label) < 60:
                        tg_list.append(str(label).strip())
                        break
            if re.findall(email_regex, label):
                # print(email_regex, label)
                if len(label) < 60:
                    email_list.append(label)
        print('label',label_list)
        print('匹配数据',list(set(wx_list)), list(set(qq_list)), list(set(tg_list)), list(set(email_list)))
        return list(set(wx_list)), list(set(qq_list)), list(set(tg_list)), list(set(email_list))

    except Exception as e:
        print(e.__traceback__.tb_frame.f_globals['__file__'], e.__traceback__.tb_lineno, e)
        return None

if __name__ == '__main__':
    # get_importinfo("http://comingzoo.com/")
    # # 无头浏览器
    # url = "https://v663.me/pc/home"

    ht_str = """
          <body>
          <div>
             </p>
    <p> <strong>E-mail: ComingZOO@gmail.com</strong><br>
                  <a href="http://wpa.qq.com/msgrd?V=1&amp;Uin=1277981160&amp;Site=ComingZOO.com全球服飾批發網&amp;Menu=yes" target="_blank"><img src="http://wpa.qq.com/pa?p=1:1277981160:4" height="16" border="0" alt="QQ"> 
      1277981160</a> 
                  <a href="http://wpa.qq.com/msgrd?V=1&amp;Uin=763997839&amp;Site=ComingZOO.com全球服飾批發網&amp;Menu=yes" target="_blank"><img src="http://wpa.qq.com/pa?p=1:763997839:4" height="16" border="0" alt="QQ"> 
      763997839</a> 
                      <img src="http://www.okonlineshop.com/logo/line.jpg" width="18" height="18" border="0" alt="LINE">LINE:comingzoo 
                      <img src="http://www.okonlineshop.com/logo/whatsapp.png" width="18" height="18" border="0" alt=" WhatsApp"> 
      WhatsApp:+852 91478002 
                      <img src="http://www.okonlineshop.com/logo/wechat.png" width="18" height="18" border="0" alt="WECHAT"> 
      微信WeChat:comingzoo                        <br>
           </p>
          </div>
          </body>
          """
    ht_ = "怒发冲冠，凭栏处、潇潇雨歇。抬望眼、仰天长啸，壮怀激烈。三十功名尘与土，八千里路云和月。莫等闲、白了少年头，空悲切。靖康耻，犹未雪。臣子恨，何时灭。驾长车，踏破贺兰山缺。壮志饥餐胡虏肉，笑谈渴饮匈奴血。待从头、收拾旧山河，朝天阙"
    soup = BeautifulSoup(ht_, 'lxml')
    print(soup.prettify())


