x = int(input("How many Fibonacci numbers to generate?: "))

if (x < 2 ):

	quit()

seq = [1,1]

def appendSumOfPastTwo(a):

	last = a[len(a) - 1] 

	secondLast = a[len(a) - 2]

	seq.append(last + secondLast)



for i in range(x - 2):

	appendSumOfPastTwo(seq)

print(seq)


