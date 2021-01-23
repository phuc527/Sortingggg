def insertion_sort(arr):
	for i in range(1,len(arr)):
		for j in range(i-1,-1,-1):
			if arr[j] > arr[j+1]:
				arr[j],arr[j+1] = arr[j+1],arr[j]
			# else:
			# 	break
	print(arr)

A = ['1','4','2','5','6','3','3']
insertion_sort(A)
A.sort()
print(A)