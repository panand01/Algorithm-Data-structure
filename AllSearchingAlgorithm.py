def fac(num):
	if(num == 1):
		return 1
	else:
		return num * fac(num - 1)

out = fac(5)
print(out)

def power(base, exponent):

	if(exponent == 0):
		return 1

	if(exponent == 1):
		return base
	else:
		return base * power(base, exponent - 1)

out = power(2,0)
print(out)

def productofarray(arr):

	if(len(arr) == 0):
		return 1
	else:
		return arr[0] * productofarray(arr[1:])

arr1 = [1,2,3,10]
out = productofarray(arr1)
print(out)

def RecursiveRange(num):
	if num == 1:
		return 1
	else:
		return num + RecursiveRange(num - 1)

out = RecursiveRange(6)
print(out)

def fib(num):

	if(num <= 2):
		return 1
	else:
		return fib(num - 1) + fib(num - 2)

out = fib(6)
print(out)


def Reverse(string):

	new_string = ""

	if(len(string) == 0):
		return new_string
	else:
		new_string = string[-1]

	new_string = new_string + Reverse(string[:(len(string) - 1)])
	return new_string

out = Reverse("rithmschool")
print(out)

def ispalindrome(string):

	def Reverse(helperstring):
		new_string = ""

		if(len(helperstring) == 0):
			return new_string
		else:
			new_string = helperstring[-1]

		new_string = new_string + Reverse(helperstring[:(len(helperstring) - 1)])
		return new_string

	n_s = Reverse(string)

	return (string == n_s)

out = ispalindrome("tacocat")
print(out)


def flatten(arr):
	flatten_arr = []

	if(len(arr1) == 0):
		return flatten_arr
	
	if(len(arr[0]) != 1):
		flatten_arr = flatten_arr.append(flatten_arr(arr[0]))
	else:
		flatten_arr.append(arr[0])
		flatten(arr[1:])

def linearSearch(arr, value):
	
	for i in range(len(arr)):
		if(arr[i] == value):
			return i

	return -1

print(linearSearch(["math", "physics", "chemistry"], "maths"))

import math
def BinarySearch(arr, value):

	mid = arr[math.floor((len(arr) - 1)/ 2)]

	if(value > mid):
		new_arr = arr[(math.floor((len(arr) - 1)/ 2) + 1):]
		print(new_arr)
		if(len(new_arr) != 0):
			BinarySearch(new_arr, value)
		else:
			print("False")
		
	elif(value < mid):
		new_arr = arr[:math.floor((len(arr) - 1)/ 2)]
		print(new_arr)
		if(len(new_arr) != 0):
			BinarySearch(new_arr, value)
		else:
			print("False")
		
	else:	
		print("True")

BinarySearch([2,3,7,9,25,40,45,48,53,58,61,63,65,69,79,88], 88)

import math
def binarysearch(arr, value):

	start = 0
	end = len(arr) - 1

	mid = math.floor((start + end) / 2)

	while( arr[mid] != value and start <= end):
		if(value > arr[mid]):
			start = mid + 1
		else:
			end = mid - 1

		mid = math.floor((start + end) / 2)

	if(value == arr[mid]):
		return mid
	else:
		return -1

out = binarysearch([2,4,6,7,9,12,15,16,19,20,28,37,38,47,49,50], 50)
print(out)

def stringsearch(astring):
	list_of_string = []
	i = 0

	while (astring[i] != "."):
		ele = ""
		while (astring[i] != " " and astring[i] != "."):
			ele = ele + astring[i]
			i = i + 1

		
		if(astring[i] == "."):
			break 
		list_of_string.append(ele)
		i = i + 1

	return list_of_string

out = stringsearch("I like to read about current economics.")
print(out)

def StringSearch(longstring, shortstring):

	i = 0
	num = 0
	while i < len(longstring):
		
		ele = ""
		for j in range(len(shortstring)):
			if(shortstring[j] == longstring[i]):
				i = i + 1
				ele = ele + shortstring[j]
				
			else:
				i = i + 1
				break
		if(ele == shortstring):
			num = num + 1

	return num


out = StringSearch("lorie loled", "lol")
print(out)


def bubblesort(arr):
	com = len(arr) - 1

	for i in range(len(arr) - 1):
		noswap = True
		for j in range(com):
			print(arr,arr[j],arr[j + 1])
			if(arr[j] > arr[j + 1]):
				# temp = arr[j]
				# arr[j] = arr[j + 1]
				# arr[j + 1] = temp
				[arr[j], arr[j + 1]] = [arr[j + 1],arr[j]]
				noswap = False

		if(noswap):
			break

		com = com - 1

	return arr

out = bubblesort([8,1,2,3,4,5,6,7])
print(out)

def selectionsort(arr):
	com = len(arr)

	for i in range(len(arr) - 1):
		smallest = arr[i]
		ind = i 
		for j in range(i,len(arr) - 1):
			print(arr)
			if(smallest > arr[j + 1]):
				ind = j + 1
				smallest = arr[ind]
				print(arr[ind])
		if(ind != i):
			[arr[i], arr[ind]] = [arr[ind], arr[i]]
		
	return arr

out = selectionsort([17,83,21,2,32,4,35,86])
print(out)

def mergearray(arr1, arr2):
	result = []
	i = 0
	j = 0

	while i < len(arr1) and j < len(arr2):

		if(arr1[i] > arr2[j]):
			result.append(arr2[j])
			j = j + 1
		else:
			result.append(arr1[i])
			i = i + 1

	if(i <= (len(arr1) - 1)):
		for i in arr1[i:]:
			result.append(i)
	else:
		for j in arr2[j:]:
			result.append(j)

	return result

out = mergearray([1,10,50], [2,14,99,100])
print(out)
out = mergearray([72],[73])
print(out)

import math
def mergesort(arr):
	if(len(arr) <= 1):
		return arr

	mid = math.floor(len(arr) / 2)
	
	left = mergesort(arr[:mid])
	right = mergesort(arr[mid:])

	print(mergearray(left, right))
	return mergearray(right, left)

out = mergesort([10,24,76,73,72,1,9])
print(out)


def quicksort(arr):
	if(len(arr) == 1):
		return arr
	index = []

	pivot = arr[0]
	i = 1

	while i < len(arr):
		if(arr[i] > pivot):
			index.append(i)
		else:
			if(len(index) != 0):
				last_index = index[0]

				[arr[index[0]], arr[i]] = [arr[i], arr[index[0]]]
				index.remove(index[0])
				index.append(i)

	[pivot,arr[last_index]] = [arr[last_index], pivot]

	left = quicksort(arr[:last_index])
	right = quicksort(arr[last_index:])

	print(mergearray(left,right))
	return mergearray(left,right)

	out = quicksort([19,28,21,30,3,6,9,4])
	print(out)
