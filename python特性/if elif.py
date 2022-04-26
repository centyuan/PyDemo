

d={
"tempname":"ctf比赛",
"firewall":[{
   "rulesetname":"规则集ctf比赛",
   "rulesetUuid":"uuid",
   "type":"Ingress",
   "target_network":"192.168.1.0/24"}],
"security":[{
		"target_network": "192.168.1.0/24",
         "protocol":"0",
          "type": "Ingress",
          "s_port":"90",
           "e_port":"100",
            "allow_network":"192.168.1.1/24"}]
}
if d.get("firewall"):
    print("firewall")
    print(d)
elif d.get("security"):
    print("security")