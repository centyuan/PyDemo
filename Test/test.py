

import difflib
str1 = "李白"
str2 = "李白 唐朝人 ？。"
# 使用SequenceMatcher()类计算两个字符串的相似度
matcher = difflib.SequenceMatcher(None, str1, str2)
diff = matcher.get_opcodes()
# 输出不同的部分
for opcode, i1, i2, j1, j2 in diff:
    if opcode == 'equal':
        print("equal:",str1[i1:i2])
    elif opcode == 'insert':
        print("insert:","\033[31m" + str2[j1:j2] + "\033[0m")
    elif opcode == 'delete':
        print("delete:","\033[32m" + str1[i1:i2] + "\033[0m")