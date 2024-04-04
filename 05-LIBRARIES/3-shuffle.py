from random import shuffle
cards = [1,2,3,4,5,6,7,8,9,'Jack', "Queen", "King"]
shuffle(cards)
for i in range(len(cards)):
    if i == len(cards) - 1:
        print(cards[i], end='')
    else:
        print(cards[i], end=' - ')
print()
