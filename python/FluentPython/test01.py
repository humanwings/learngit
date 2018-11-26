from FrenchDeck import FrenchDeck
from FrenchDeck import Card
from FrenchDeck import spades_high
from random import choice

beer_card = Card('7', 'diamonds')
print(beer_card)

# FrenchDeck实现了 __len__和 __getitem__，所以是一个序列(seq)
deck = FrenchDeck()

print(len(deck))
print(deck[0])
print(deck[37])

# 随机抽选, choice适用于序列(seq)
print(choice(deck))
print(choice(deck))

# for card in deck:
#     print(card)

print(Card('Q', 'hearts') in deck)

# 排序
for card in sorted(deck, key=spades_high):
    print(card)