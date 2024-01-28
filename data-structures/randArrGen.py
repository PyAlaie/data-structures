import random

def random_list(n=10, a=0, b=20):
    return [random.randint(a,b) for i in range(n)]

def random_permutation(a=0,b=10):
    l = [i for i in range(a,b)]
    random.shuffle(l)
    return l

def random_strings(count=10, string_size=5):
    chars = [chr(i) for i in range(97,123)]
    
    res = []
    for i in range(count):
        a = ''.join(random.choices(chars, k=string_size))
        res.append(a)
    
    return res

# def random_same_len_ints(count=10, max_digits=5)