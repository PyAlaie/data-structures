def counting_sort(A, k, n):  
    C = [0] * (k+1)
    B = [0] * n
    
    for i in range(n):
        C[A[i]] += 1

    for i in range(1, k+1):
        C[i] +=  C[i-1]
    
    for i in range(n-1, -1, -1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1
    
    return B

def modified_counting_sort(A, k, n): # works also for negative numbers
    m = min(A)
    offset = 0-m
    l = [i+offset for i in A]
    
    C = [0] * (k+1+offset)
    B = [0] * n

    for i in range(n):
        C[l[i]] += 1

    for i in range(1, k+1+offset):
        C[i] +=  C[i-1]
    
    for i in range(n-1, -1, -1):
        B[C[l[i]]-1] = l[i] - offset
        C[l[i]] -= 1
    
    return B

if __name__ == '__main__':
    import randArrGen
    
    random_array = randArrGen.random_permutation()
    
    print("Before:", random_array)
    random_array = counting_sort(random_array, max(random_array), len(random_array))
    print("After: ", random_array)
    