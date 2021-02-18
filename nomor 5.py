#michelle adelia suwarno / xi mia 1 / 25
import itertools, random

deck = list(itertools.product(range(1,14), ['kriting', 'hati', 'wajik', 'sekop']))

random.shuffle(deck)
print("kamu mendapat :")
for i in range(5) :
    print(deck[i][0],' dari ', deck[i][1])