def merge(arr, l, m, r):
	nl = m - l + 1
	nr = r - m

	left = [0] * nl
	right = [0] * nr
 
	for i in range(nl):
		left[i] = arr[l + i]

	for j in range(nr):
		right[j] = arr[m + j+1]

	i = 0
	j = 0
	k = l

	while i < nl and j < nr:
		if left[i] <= right[j]:
			arr[k] = left[i]
			i += 1
		else:
			arr[k] = right[j]
			j += 1
		k += 1

	while i < nl:
		arr[k] = left[i]
		i += 1
		k += 1

	while j < nr:
		arr[k] = right[j]
		j += 1
		k += 1

def mergeSort(arr, l, r):
	if l < r:
		m = (r+l)//2
  
		mergeSort(arr, l, m)
		mergeSort(arr, m+1, r)
		merge(arr, l, m, r)

if __name__ == '__main__':
    import random
    
    random_list = [random.randint(0,50) for i in range(10)]
    
    print("Before Sort:", random_list)
    
    mergeSort(random_list, 0, len(random_list)-1)
    
    print("After Sort: ", random_list)
	