import os
import requests
from bs4 import BeautifulSoup
import jieba
#https://zhuanlan.zhihu.com/p/349955626

def download_video(video_url):
    '''
      youget 下载视频
      :param video_url:视频链接
      :param save_path: 保存路径
      :param video_name: 视频命名
      :return:
      '''
    # you-get -o 输出文件路径
    # you-get -O 输出文件名称
    # you-get -l [URL] 下载视频列表
    cmd = 'you-get {}'.format(video_url)
    # os.popen() 方法用于从一个命令打开一个管道。
    os.popen("D:\python_data\centyuan\cent30\Scripts\activate.bat",)
    res = os.popen(cmd,)
    #获取弹幕接口http://comment.bilibili.com/{cid}.xml # cid 为B站视频的cid 编号cid=419950348

def download_danmu():
    """
    弹幕下载并分词存储
    :return:
    """
    cid = "419950348"
    danmu_url = "http://comment.bilibili.com/{}.xml".format(cid)
    f = open("danmu.txt","w+",encoding="utf-8")
    res = requests.get(danmu_url)
    res.encoding = "utf-8"
    soup = BeautifulSoup(res.txt,'lxml')
    items = soup.find_all('d') #找到所有d标签
    for item in items:
        text = item.text
        print(text)
        seg_list = jieba.cut(text,cut_all=True) #对字符串进行分词处理，方便后面制作词云图
        for j in seg_list:
            print(j)
            f.write(j)
            f.write('\n')
    f.close()


def main():
    download_video("https://www.bilibili.com/video/BV1ZY411j7DT?spm_id_from=333.1073.channel.secondary_floor_video.click")

if __name__ == '__main__':
    main()