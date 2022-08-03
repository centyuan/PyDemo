import json
import os
import random
import time
import zipfile
from time import time

import requests
from bson import ObjectId

from app.config import Config
from app.utils.conn import conn_db


class shellDetector:
    # 壳识别
    def __init__(self):
        self.shellfeatures = {
            "libchaosvmp.so": u"娜迦",
            "libddog.so": u"娜迦",
            "libfdog.so": u"娜迦",
            "libedog.so": u"娜迦企业版",
            "libexecmain.so": u"爱加密",
            "ijiami.dat": u"爱加密",
            "ijiami.ajm": u"爱加密企业版",
            "libsecexe.so": u"梆梆免费版",
            "libsecmain.so": u"梆梆免费版",
            "libSecShell.so": u"梆梆免费版",
            "libDexHelper.so": u"梆梆企业版",
            "libDexHelper-x86.so": u"梆梆企业版",
            "libprotectClass.so": u"360",
            "libjiagu.so": u"360",
            "libjiagu_art.so": u"360",
            "libjiagu_x86.so": u"360",
            "libegis.so": u"通付盾",
            "libNSaferOnly.so": u"通付盾",
            "libnqshield.so": u"网秦",
            "libbaiduprotect.so": u"百度",
            "aliprotect.dat": u"阿里聚安全",
            "libsgmain.so": u"阿里聚安全",
            "libsgsecuritybody.so": u"阿里聚安全",
            "libmobisec.so": u"阿里聚安全",
            "libtup.so": u"腾讯",
            "libexec.so": u"腾讯",
            "libshell.so": u"腾讯",
            "mix.dex": u"腾讯",
            "lib/armeabi/mix.dex": u"腾讯",
            "lib/armeabi/mixz.dex": u"腾讯",
            "libtosprotection.armeabi.so": u"腾讯御安全",
            "libtosprotection.armeabi-v7a.so": u"腾讯御安全",
            "libtosprotection.x86.so": u"腾讯御安全",
            "libnesec.so": u"网易易盾",
            "libAPKProtect.so": u"APKProtect",
            "libkwscmm.so": u"几维安全",
            "libkwscr.so": u"几维安全",
            "libkwslinker.so": u"几维安全",
            "libx3g.so": u"顶像科技",
            "libapssec.so": u"盛大",
            "librsprotect.so": u"瑞星"
        }

    def shell_detector(self, apk_path):
        zipfiles = zipfile.ZipFile(apk_path)
        nameList = zipfiles.namelist()

        for fileName in nameList:
            try:
                for shell in self.shellfeatures.keys():
                    if shell in fileName:
                        shellType = self.shellfeatures[shell]
                        print(u"经检测，该apk使用了" + shellType + u"进行加固")
                        return True, shellType
            except:
                return False, u"unknown"
        return False, u"未加壳"


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
    "User-Agent": random.choice(user_agent_list)
}


def perimission_translation(res):
    json_report = dict(json.loads(res.text))
    permissions = json_report.get("permissions")  # {key:{value}
    new_permissions = permissions
    # zh_permissios_file = open('permission权限集.md', 'r', encoding='utf-8')
    zh_permissios_file = open(os.path.dirname(__file__) + '/permission权限集.md', 'r', encoding='utf-8')
    # print('目录', os.path.dirname(__file__) + '/permission权限集.md')
    dd = [it + '}' for it in zh_permissios_file.readlines()[0].split('},')]
    for key, value in permissions.items():
        for it in dd:
            if key in it:
                it_dict = json.loads(it)
                middle_data = permissions[key]
                middle_data['info'] = it_dict['类型']
                middle_data['description'] = it_dict['详细情况']
                if permissions[key]['status'] == 'dangerous':
                    middle_data['status'] = '危险'
                elif permissions[key]['status'] == 'normal':
                    middle_data['status'] = '正常'
                else:
                    middle_data['status'] = '未知'
                new_permissions[key] = middle_data
                print(new_permissions[key])

    print('apk分析:translation over', new_permissions)
    json_report['permissions'] = new_permissions
    return json.dumps(json_report)


def upload_apk(ips, apk_data):
    # upload_url = "http://106.75.252.48:32328/api/v1/upload"
    try:
        upload_url = ips + "/api/v1/upload"

        apk_file = open(str(apk_data['file_path']), 'rb')
        files = {
            "file": (apk_data["apk_name"], apk_file, 'multipart/form-data')  # 名字
        }
        print('apk分析:上传应用apk', upload_url, apk_data, files)
        res = requests.post(upload_url, files=files, headers=headers)
        print('apk分析:上传返回:', res.status_code, res.text)
        result = json.loads(res.text)
        apk_file.close()
        return True, result
    except Exception as e:
        print(e.__traceback__.tb_frame.f_globals["__file__"], e.__traceback__.tb_lineno, e)
        return False, e


def start_scan(ips, result):
    # scan_url = 'http://106.75.252.48:32328/api/v1/scan'
    scan_url = ips + '/api/v1/scan'
    scan_data = {
        'scan_type': result.get("scan_type"),
        'file_name': result.get("file_name"),
        'hash': result.get("hash"),
        # 're_scan':''
    }
    print('apk分析:开始分析', scan_data)
    try:
        res = requests.post(scan_url, data=scan_data, headers=headers, timeout=3)
    except requests.exceptions.ReadTimeout as e:
        print('apk分析:请求start_scan返回e', e)


def get_json(ips, hash):
    json_url = ips + '/api/v1/report_json'
    json_data = {
        'hash': hash
    }
    res = requests.post(json_url, data=json_data, headers=headers)
    print('apk分析:获取json报告', json_data, res)
    return res


def download_pdf(ips, hash):
    down_url = ips + '/api/v1/download_pdf'
    down_data = {
        'hash': hash
    }

    res = requests.post(down_url, data=down_data, headers=headers)
    print('res.headers', res.headers)
    print('res', res.text)


def recent_scan(ips):
    re_url = ips + "/api/v1/scans"
    kw = {
        'page': '1',
        'page_size': '100',
    }
    res = requests.get(re_url, params=kw, headers=headers)
    print('apk分析:最近扫描')
    print(json.loads(res.text))


def delete_scan(ips, scan_hash):
    # headers = {
    #     "Authorization": "12223eac239e7061c35f4a74029643c9cf9b84b6dff2c3d5d29c2b8455efde5e",
    #     "User-Agent": random.choice(user_agent_list)
    # }
    delete_url = ips + "/api/v1/delete_scan"
    data = {
        'hash': scan_hash,
    }
    res = requests.post(delete_url, data=data, headers=headers)
    print("apk分析:删除scan", res, res.text)


def apk_analysis(apk_data):
    apk_obj = conn_db('apk').insert_one(apk_data)
    # ips = "http://149.28.210.253:9633"
    ips = Config.APK_ANALYSIS
    print("apk分析：1.异步apk分析")
    try:
        try:
            sd = shellDetector()
            shell_re = sd.shell_detector(apk_data["file_path"])[1]
            if shell_re:
                conn_db('apk').update_one({'_id': ObjectId(apk_obj['_id'])}, {"$set": {"shell_type": shell_re}})
        except Exception as e:
            print(e.__traceback__.tb_frame.f_globals["__file__"], e.__traceback__.tb_lineno, e)
            conn_db('apk').update_one({'_id': ObjectId(apk_obj['_id'])},
                                      {"$set": {"description": str(e), "shelltype": "未加壳"}})

        code, result = upload_apk(ips, apk_data)
        if code:
            data = {
                # 'scan_type': result.get("scan_type"),
                'file_name': result.get("file_name"),
                'hash_value': result.get("hash")
            }
            print('apk分析:2.记录apk_info hash_value:', data)
            conn_db('apk').update_one({'_id': ObjectId(apk_obj['_id'])},
                                      {"$set": data})
            start_scan(ips, result)
        else:
            conn_db('apk').update_one({'_id': ObjectId(apk_obj['_id'])},
                                      {"$set": {"description": "apk上传失败", "status": 3}})
        for i in range(100):
            print(f"apk分析:3.获取{apk_data['apk_name']}apk分析json结果:{i}")
            res = get_json(ips, result.get("hash"))
            if res.status_code == 200:
                content = perimission_translation(res)
                apk_info = conn_db('apk').find({'_id': ObjectId(apk_obj['_id'])})
                apk_info['content'] = content
                apk_info['description'] = str(i) + "次循环"
                conn_db('apk').update_one({'_id': ObjectId(apk_obj['_id'])}, {"$set": apk_info})
                print("apk分析:4.保存json结果", apk_info)
                break
            elif i == 99 and res.status_code == 404:
                conn_db('apk').update_one(
                    {'_id': ObjectId(apk_obj['_id'])},
                    {"$set": {'status': 3, 'description': "超时timeout"}})
            time.sleep(60)

    except Exception as e:
        print(e.__traceback__.tb_frame.f_globals["__file__"], e.__traceback__.tb_lineno, e)
        conn_db('apk').update_one({'_id': ObjectId(apk_obj['_id'])}, {"$set": {'status': 3, 'description': e}})
