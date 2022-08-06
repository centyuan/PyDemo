import requests
import json
import random

user_agent_list = [
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/61.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15", ]

headers = {
    "Authorization": "b3122ecfa944777a69c9a3e899cbf1c041f67151f16ce3780323444e02ce3f15",
    "User-Agent":random.choice(user_agent_list)
}

def upload_apk(ips,name):
    # # 上传
    # upload_url = "http://106.75.252.48:32328/api/v1/upload"
    upload_url = ips+"/api/v1/upload"
    print("upload_url",upload_url)
    apk_file = open(name, 'rb')
    # ['application/octet-stream', 'application/vnd.android.package-archive', 'application/x-zip-compressed', 'binary/octet-stream']
    files = {
        # cn.jiage315.chayao_4.0.6_406
        "file":(name,apk_file,'application/octet-stream') # 名字
    }
    # res = requests.post(upload_url,files=files,headers=headers,proxies=proxies)
    res = requests.post(upload_url,files=files,headers=headers)
    print('返回',res.status_code,res.text)
    result = json.loads(res.text)
    print("上传返回",result)
    apk_file.close()
    return result
def start_scan(ips,result):
    # 扫描
    # scan_url = 'http://106.75.252.48:32328/api/v1/scan'
    scan_url = ips+'/api/v1/scan'

    print("scan_url",scan_url)
    scan_data = {
        'scan_type':result.get("scan_type"),
        'file_name':result.get("file_name"),
        'hash':result.get("hash"),
        #'re_scan':''
    }
    print('开始分析',scan_data)
    res = ''
    try:
        res = requests.post(scan_url,data=scan_data,headers=headers,timeout=3)
    except requests.exceptions.ReadTimeout as e:
        print(e)
        print('分析返回',res)


def get_json(ips,hash):
    # json报告
    json_url = ips+'/api/v1/report_json'
    json_data = {
        'hash':hash
    }
    res = requests.post(json_url,data=json_data,headers=headers)

    print('请求头',res.request.headers)
    print(json.loads(res.text))
    with open('json.txt','w+',encoding='utf-8') as f:
        f.write(res.text)
        print('aaaaaaa')
    return res


def download_pdf(ips,hash):
    # 下载pdf
    down_url = ips+'/api/v1/download_pdf'
    down_data = {
        'hash': hash
    }

    res = requests.post(down_url,data=down_data,headers=headers)
    print('res.headers',res.headers)
    print('res',res.text)

def recent_scan(ips):
    re_url = ips+"/api/v1/scans"
    kw = {
        'page':'1',
        'page_size':'100',
    }
    res = requests.get(re_url,params=kw,headers=headers)
    print('最近扫描')
    print(json.loads(res.text))

def delete_scan(ips,hash):
    headers = {
        "Authorization": "12223eac239e7061c35f4a74029643c9cf9b84b6dff2c3d5d29c2b8455efde5e",
        "User-Agent": random.choice(user_agent_list)
    }
    delete_url = ips+"/api/v1/delete_scan"
    data = {
        'hash':hash,
    }
    res = requests.post(delete_url,data=data,headers=headers)
    print("删除scan",res,res.text)

if __name__ == '__main__':
    # result = upload_apk('douyu_v6.2.1.apk')
    import time
    # ips = "http://149.28.210.253:9633"
    ips = "http://45.77.168.10:8000"
    # result = upload_apk(ips,'46454e6f63cfa9f41dc61e2cc694ca6b.apk')
    # start_scan(ips,result)

    result = {"hash":'46454e6f63cfa9f41dc61e2cc694ca6b'}
    for i in range(100):
        print("获取json报告")
        get_json(ips,result.get("hash")) # com.ireadercity_5.56.6_5566.apk
        time.sleep(60)


    # json_report = dict(json.loads(res.text))
    # test = '{"host_os": "nix", "timestamp": "2022-06-18T09:57:59.270Z"}'
    #
    # abc = test.replace('\'',"\"")
    # print(abc,json.loads(abc))
    # print(json.loads('{"name":"name","sex":"nan"}'))
    # json_report = open('json_report.txt','r',encoding='utf-8').read()
    # dd = dict(json_report)
    # print(type(dict(dd)))
    # permissions = json_report.get("permissions") # {key:{value}
    # new_permissions = permissions
    # print("读取permisssions")
    # print('权限',permissions)
    # zh_permissios_file = open('permission权限集.md','r',encoding='utf-8')
    # dd = [it+'}' for it in zh_permissios_file.readlines()[0].split('},')]
    # # {'android.permission.ACCESS_NETWORK_STATE': {'status': 'normal', 'info': 'view network status', 'description': 'Allows an application to view the status of all networks.'},android.p
    # or_d = {"向手机申请的权限":"android.permission.READ_LOGS","类型":"读取系统日志","详细情况":"读取系统底层日志","是否危险":"正常"}
    # for key,value in permissions.items():
    #     for it in dd:
    #          if key in it:
    #             it_dict = json.loads(it)
    #             middle_data = permissions[key]
    #             middle_data['info'] = it_dict['类型']
    #             middle_data['description'] = it_dict['详细情况']
    #             if permissions[key]['status'] =='dangerous':
    #                 middle_data['status'] = '危险'
    #             else:
    #                 middle_data['status'] = '正常'
    #             print('中间数据',middle_data)
    #             new_permissions[key] = middle_data
    #             print(new_permissions[key])
    # print(new_permissions)
    # json_report['permissions'] = new_permissions
    # with open('sffffff.txt','w',encoding='utf-8') as f:
    #     f.write(str(json_report))
    # print(json_report)
    #
