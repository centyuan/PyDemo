"""
question:求字符串数组里，最长公共前缀
thinking:
1.排序(长度，有相同的前缀,)
2.比较最小的和最大的相同位置值是否一致

"""

def longest_common_prefix(strs):
    # strs.sort(key=lambda item:len(item)) # 按长度排序
    strs.sort()                            # 按大小排序
    print('排序后',strs)
    min_length = strs[0]
    max_length = strs[-1]
    s = ""
    for i in range(len(min_length)):
        if i < len(max_length) and min_length[i]==max_length[i]:
            s += min_length[i]
        else:
            break
    return s

strs = ['abc123frqw','abc124asfd','abc','ab1234123a','agfwee']
result = longest_common_prefix(strs)
print('result:',result)