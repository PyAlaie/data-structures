def left(i):
    return 2*i + 1

def right(i):
    return 2*i + 2

def max_heapify(A, n, i):
    l = left(i)
    r = right(i)
    
    largest = i
    if l < n and A[l] > A[i]:
        largest = l
    if r < n and A[r] > A[largest]:
        largest = r
    
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, n, largest)
        
def build_max_heap(A, n):
    for i in range(n//2, -1, -1):
        max_heapify(A, n, i)
        
def heap_sort(A, n):
    heap_size = n
    build_max_heap(A, n)
    for i in range(n-1, 0, -1):
        A[i], A[0] = A[0], A[i]
        heap_size -= 1
        max_heapify(A, heap_size, 0)
    
if __name__ == '__main__':
    import randArrGen
    
    random_array = randArrGen.random_permutation()
    
    print("Before:", random_array)
    heap_sort(random_array, len(random_array))
    print("After: ", random_array)