def insertion_sort(array, n):
    for i in range(1, n):
        key = array[i]

        j = i - 1
        while j >= 0 and array[j] > key:
            array[j+1] = array[j]
            j -= 1
            
        array[j+1] = key

if __name__ == '__main__':
    import random
    
    random_list = [random.randint(0,50) for i in range(10)]
    
    print("Before Sort:", random_list)
    
    insertion_sort(random_list, len(random_list))
    
    print("After Sort: ", random_list)
    