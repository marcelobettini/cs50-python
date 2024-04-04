# import random -> random.choice()
times=19
from random import choice
endResult = {
    'heads':0, 
    'tails':0
    }
for i in range(times):
    flip = choice(['heads', 'tails'])
    endResult[flip]+=1
    print(flip, end=' - ')

print(f'\nstatistics: \nheads: { round(endResult["heads"] / times * 100,1)}%\ntails: {round(endResult["tails"] / times * 100,1)}%')

