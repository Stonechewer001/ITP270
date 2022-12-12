examList = []
n = int(input("Enter the number of scores : "))
for i in range(0,n):
	exam = int(input())

	examList.append(exam)

def Average(examList):
	return sum(examList) / len(examList)

average = Average(examList)
total = sum(examList)
high = max(examList)
examList.sort()

examListTwo = []
m = len(examList)
for i in range(0,m):
	exam2 = int(input())

	examListTwo.append(exam2)

list(zip(examList, examListTwo))
print (list(zip(examList, examListTwo)))

def listSum():
	sum(examListTwo)
	print(sum(examListTwo))

print (average)
print (total)
print (high)
print (examList)
listSum()
