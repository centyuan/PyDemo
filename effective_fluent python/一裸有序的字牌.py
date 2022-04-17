import collections

#collections.namedtuple 构建了一个简单的类来表示一张纸牌
"""
以两个下划线结尾（例如__getitem__）。
比如obj[key] 的背后就是__getitem__ 方法，
"""
#1.创建Card 类 表示纸牌
Card = collections.namedtuple('Card',['rank','suit'])
beer_card = Card('7','diamonds')
print(beer_card)   #输出 Card(rank='7',suit='diamonds')
#2.创建 FrenchDeck类，实现一些方法
class FrenchDeck: #python3默认继承object
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    #spades 黑桃 diamonds方片 clubs梅花 hearts红心
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank,suit) for suit in self.suits
                                       for rank in self.ranks
                       ]
    def __len__(self):
        return len(self._cards)
    def __getitem__(self, position):
        return self._cards[position]
deck = FrenchDeck()
#3.实现len
print(len(deck)) #len() 函数来查看一叠牌有多少张
#4 随机抽取一张纸牌
from random import choice
print(choice(deck))

#5.deck类自动支持切片(slicing)
print(deck[:3])
#6.仅仅实现了__getitem__ 方法，这一摞牌就变成可迭代的了
for card in deck:
    print(card)
for card in reversed(deck): #反向迭代
    print(card)
#6.排序
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) +suit_values[card.suit]
for card in sorted(deck,key=spades_high):
    print('排序:',card)
