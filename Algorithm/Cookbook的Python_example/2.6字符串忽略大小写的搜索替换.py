import re

"""
传入re.IGNORECASE参数
"""
text = "UPPER PYTHON，lower python ,Mixed Python"
print(re.findall('python',text,flags=re.IGNORECASE))
# ['PYTHON', 'python', 'Python']

new_text = re.sub('python','java',text,flags=re.IGNORECASE)
print(new_text)
# UPPER java，lower java ,Mixed java

# 自动跟被匹配字符串的大小写保持一致。
def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
              return word.upper()
        elif text.islower():
              return word.lower()
        elif text[0].isupper():
             return word.capitalize()
        else:
             return word
    return replace

new_text = re.sub('python', matchcase('java'), text, flags=re.IGNORECASE)
print(new_text)
# UPPER JAVA，lower java ,Mixed Java
