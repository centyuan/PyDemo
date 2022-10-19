from DecryptLogin import login

# the instanced client
client = login.Client()
# the instanced weibo
weibo = client.weibo(reload_history=True)
# use the login function to login in weibo
infos_return, session = weibo.login('me', 'pass', 'scanqr')