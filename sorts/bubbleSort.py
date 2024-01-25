def bubble_sort(array, n):
    for i in range(n):
        for j in range(n-1,i,-1):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
                
def modified_bubble_sort(array, n): # this one would have linear time on sorted arrays
    for i in range(n):
        changed = False
        for j in range(0,n-i-1):
            if array[j] > array[j+1]:
                changed = True
                array[j+1], array[j] = array[j], array[j+1]
        if not changed:
            break
                
if __name__ == '__main__':
    import random
    
    random_list = [random.randint(0,50) for i in range(10)]
    
    print("Before Sort:", random_list)

    modified_bubble_sort(random_list, len(random_list))
    
    print("After Sort: ", random_list)