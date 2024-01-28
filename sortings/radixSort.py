def counting_sort(arr, exp1):
    n = len(arr)
 
    output = [0] * (n)
 
    count = [0] * (10)
 
    for i in range(0, n):
        index = arr[i] // exp1
        count[index % 10] += 1
 
    for i in range(1, 10):
        count[i] += count[i - 1]
 
    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
 
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]
 
def radix_sort(arr):
    max1 = max(arr)
 
    exp = 1
    while max1 / exp >= 1:
        counting_sort(arr, exp)
        exp *= 10
        
if __name__ == '__main__':
    import randArrGen

    random_array = randArrGen.random_list(20,0,30)
    
    print("Before:", random_array)
    radix_sort(random_array)
    print("After: ", random_array)
    