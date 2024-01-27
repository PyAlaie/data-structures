def insert(array, item):
    array.append(item)
    
    i = len(array) - 1
    while array[i] < array[i-1] and i > 0:
        array[i], array[i-1] = array[i-1], array[i]
        i -= 1

def bucket_sort(A, n):
    import math
    buckets = []
    
    for i in range(n):
        buckets.append([])
        
    arr_max = max(A)
    arr_min = min(A)
    
    for i in A:
        squeezed = (i - arr_min)/(arr_max-arr_min + 0.0001) # squeeze between 0 and 1
        bucket_index = math.floor(n * squeezed)
        
        insert(buckets[bucket_index], i)
        
    res = []
    for bucket in buckets:
        res.extend(bucket)
        
    return res

if __name__ == '__main__':
    import randArrGen
    
    random_array = randArrGen.random_permutation()
    
    print("Before:", random_array)
    random_array = bucket_sort(random_array, 5)
    print("After: ", random_array)
    