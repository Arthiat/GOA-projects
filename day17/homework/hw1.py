listn = [1,2,32,5,6,7,8]

def f(listn, elementi):
    while elementi in listn:
        listn.remove(elementi)
    return listn

print(f(listn,2))