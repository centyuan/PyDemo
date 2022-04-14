import collections

#collections.namedtuple 构建了一个简单的类来表示一张纸牌
"""
以两个下划线结尾（例如__getitem__）。
比如obj[key] 的背后就是__getitem__ 方法，
"""
Card = collections.namedtuple('Card',['rank','suit'])
"""
beer_card = Card('7','diamonds')
beer_card   #输出 Card(rank='7',suit='diamonds')
"""

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank,suit) for suit in self.suits
                                       for rank in self.ranks
                       ]
    def __len__(self):
        return len(self._cards)
    def __getitem__(self, position):
        return self._cards[position]

"""
usage: deck = FrenchDeck()
       len(deck) #len() 函数来查看一叠牌有多少张
       from random import choice 
       choice(deck) #随机抽取一张纸牌
"""

