#_________________________________________________
#Sortowanie

#_________________________________________________
#Selection sort

# zlozonosc chyba O(N**2)
# moje ma 57 krokow dla podanych wartosci

def selection_sort(A):
	dlugosc = len(A)
	for i in range(dlugosc):
		for j in range(i+1, dlugosc):
			if A[j] < A[i]:
				A[i], A[j] = A[j], A[i]
	return A

A = [10,2,1,1,3,4]
print selection_sort(A)

# z tutoriala ma 68

def selection_sort(A):
	dlugosc = len(A)
	for i in range(dlugosc):
		minimal = i
		for j in range(i+1, dlugosc):
			if A[j] < A[minimal]:
				minimal = j
		A[i], A[minimal] = A[minimal], A[k]
	return A

A = [10,2,1,1,3,4]
print selection_sort(A)
#_________________________________________________
#Counting sort
# zlozonosc chyba O(N+k)

#
# popacz jeszcze, zrozum, napisz swoje, wytlumacz kogucikowi
#

def countingSort(A, k):
	n = len (A)
	count = [0]*(k + 1)
	for i in xrange(n):
		count[A[i]] += 1
	p = 0
	for i in xrange(k + 1):
		for j in xrange (count[i]):
			A[p] = i 
			p += 1
	return A

A = [10,2,1,1,3,4]
print countingSort(A, 21)

#_________________________________________________
#Merge sort
# https://www.youtube.com/watch?v=EeQ8pwjQxTM
# https://www.youtube.com/watch?v=Nso25TkBsYI
# https://www.youtube.com/watch?v=TzeBrDU-JaY
# https://www.youtube.com/watch?v=GCae1WNvnZM

#_________________________________________________
#Bubble sort
#_________________________________________________
#Insertion sort
#_________________________________________________
#Quick sort
