"""

"""
#1.
a = dict(one=1,two=2,three=3) # {'one': 1, 'two': 2, 'three': 3}
b = {'one': 1, 'two': 2, 'three': 3} #  {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one','two','three'],[1,2,3]))  #  {'one': 1, 'two': 2, 'three': 3}
d = dict([('two',2),('one',1),('three',3)])
e = dict({'three':3,'two':2,'one':1})
#a=b=c=d=e

#2.字典推导
dial_codes = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan'),
]
country_code = {country:code for code,country in dial_codes}
#{'China': 86, 'India': 91, 'United States': 1, 'Indonesia': 62, 'Brazil': 55, 'Pakistan': 92, 'Bangladesh': 880, 'Nigeria': 234, 'Russia': 7, 'Japan': 81}
