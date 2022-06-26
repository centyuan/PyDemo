def get_customer_url(url):
    try:
        user_agent_list = [
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/61.0",
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
            "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15", ]
        index_headers = {
            "User-Agent": random.choice(user_agent_list)
        }
        resp = requests.get(url, headers=index_headers)
        import re
        customer_regex = r"(http|ftp|https):\/\/([\w\-]+(\.[\w\-]+)*\/)*[\w\-]+(\.[\w\-]+)*\/?(\?([\w\-\.,@?^=%&:\/~\+#]*)+)?"
        match_url = [x.group() for x in re.finditer(customer_regex, resp.text)]
        success_url = []
        for it in match_url:
            try:
                response = requests.get(it, headers=index_headers,verify=False,timeout=3)
                if response.status_code == 200:
                    success_url.append(response.url)
            except Exception as e:
                print(e.__traceback__.tb_frame.f_globals["__file__"], e.__traceback__.tb_lineno, e)
                continue
        return success_url
    except Exception as e:
        print(e.__traceback__.tb_frame.f_globals["__file__"], e.__traceback__.tb_lineno, e)
        return None

def custom_analy(url):
    if not url.startswith("http"):
        for d in ["http://", "https://"]:
            all_url = get_customer_url(d+url)
            if all_url:
                break
    else:
        all_url = get_customer_url(url)
    return all_url