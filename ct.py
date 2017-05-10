
import random
num=51



def cointoss(num):
    attempt=0
    heads=0
    tails=0
    for x in range(1,num):
        flip = random.randint(0, 1)
        if flip>0:
            attempt+=1
            heads+=1
            print "Attempt #{}: Throwing a coin...It's a heads ... Got {} head(s) so far and {} tail(s)".format(attempt, heads, tails)

        else:
            attempt+=1
            tails+=1
            print "Attempt #{}: Throwing a coin...It's a tails ... Got {} head(s) so far and {} tail(s)".format(attempt, heads, tails)

cointoss(num)
