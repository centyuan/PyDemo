# -*- coding:utf-8 -*-
import re
from urllib import request
import xlwt
class Spider():
    url='https://www.panda.tv/cate/lol'
    info_pattern=' <div class="video-info">([\s\S]*?)</div>' #?非贪婪 ()组
    name_pattern='</i>([\s\S]*?)</span>'
    number_pattern='<span class="video-number">([\s\S]*?)</span>'
    def __fetch_content(self):

        r=request.urlopen(Spider.url)
        htmls=r.read()
        htmls=str(htmls,encoding='utf-8')
        # wenj = open('paxie.text', 'w')
        # wenj.write(self.htmls)
        # wenj.close()
        return htmls

    def __analysis(self,htmls):
        ht=re.findall(Spider.info_pattern,htmls)
        print(ht[1])
        anchors=[]
        for ht in ht:
            name=re.findall(Spider.name_pattern,ht)
            number=re.findall(Spider.number_pattern,ht)
            anchor={'name':name,'number':number}
            anchors.append(anchor)
        print(anchors[1])
        return anchors

    def __define(self,anchors):#精炼数据
        l=lambda anchor:{
            'name':anchor['name'][0].strip(),
            'number':anchor['number'][0]                  }
        return map(l,anchors)

    def __sort(self,anchors):#排序
        anchors=sorted(anchors,key=self.__sort_seed,reverse=True)
        return anchors

    def __sort_seed(self,anchor):#排序key
        r=re.findall('\d*',anchor['number'])
        number=float(r[0])
        if '万' in anchor['number']:
            number *=10000
        return number


    def __show(self,anchors):
        mybook=xlwt.Workbook(encoding='utf-8')
        mysheet=mybook.add_sheet('主播信息')
        mysheet.write(0, 0, label='name')
        mysheet.write(0, 1, label='number')
        print(type(anchors))
        print(anchors[0])
        #for anchor in anchors:
        for index in range(len(anchors)):
            #print(anchor['name']+'-----'+anchor['number'])
            print(anchors[index]['name']+'----'+anchors[index]['number'])
            mysheet.write(index+1,0,label=anchors[index]['name'])
            mysheet.write(index+1,1,label=anchors[index]['number'])
        mybook.save('主播信息.xls')

    def go(self):
        htmls=self.__fetch_content()
        anchors=self.__analysis(htmls)
        anchors=list(self.__define(anchors)) #map对象转换
        anchors=self.__sort(anchors)
        self.__show(anchors)



spider=Spider()
spider.go()
