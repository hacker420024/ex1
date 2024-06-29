import sys
def printArr(b, n):
	for i in range(0, n, 1):
		print(b[i], end = " ")
def ModifiedArray(a, n):
	l = 0
	r = sys.maxsize
	b = [0 for i in range(n)] 
	for i in range(0, int(n / 2), 1):
		b[i] = max(l, a[i] - r)
		b[n - i - 1] = a[i] - b[i]
		l = b[i]
		r = b[n - i - 1]
	printArr(b, n)
if __name__ == '__main__':
	a = [5, 6]
	n = len(a)
	ModifiedArray(a, 2 * n)
