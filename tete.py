def is_ip(address):
    try:
        ip = str(address)[:-3]
        print(ip)
        ip_str = str(ip).split('.')
        if len(ip_str) !=4:
            raise Exception("格式不正确,请输入正确格式")
            return False
        a,b,c,d = ip_str
        a, b, c, d = int(a), int(b), int(c), int(d)
        if 255>= max(a,b,c,d) and 0<=min(a,b,c,d):
            return True
        else:
            raise Exception("非法ip  {}".format(".".join(ip)))
            return False
    except Exception as e:
        return False

if __name__ == '__main__':
# player_ip = match.player_ip   # 比赛选手IP段
# user_network_segment = ip.split(".")[0:3]
# match_network_segment = player_ip.split(".")[0:3]
# if user_network_segment != match_network_segment:
#   return Response(data={"success":False, "info":"无权限加入比赛"})
    ff = is_ip('192.168.9.1/24')