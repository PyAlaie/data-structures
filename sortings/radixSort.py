def radix_sort(A, d):
    for i in range(d-1, -1,-1):
        A = sorted(A, key=lambda x : x[i])
    return A
        
if __name__ == '__main__':
    import randArrGen

    random_array = randArrGen.random_strings()
    
    print("Before:", random_array)
    random_array = radix_sort(random_array, 5)
    print("After: ", random_array)
    