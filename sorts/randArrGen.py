import random

def random_list(n=10, a=0, b=20):
    return [random.randint(a,b) for i in range(n)]

def random_permutation(a=0,b=10):
    l = [i for i in range(a,b)]
    random.shuffle(l)
    return l