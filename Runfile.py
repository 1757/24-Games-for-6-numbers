import itertools
from ReversePolish import Cal

#Number list
numlist = ['1', '6', '6', '7', '25', '75']
#((6+6 - 1/25) * 75)-7
# list "num" is used to replace the string "num1, num2" inside the file
num = ["num1", "num2", "num3", "num4", "num5", "num6"]

# x is the list of all possible operator
x = ['+', '-', '*', '/']

#This part of the code is to return Cartesian Product of x, which is all possible permutation with replacements
a= itertools.product(x, repeat=5)
opList=[]
for k in a:
	opList.append(k)
# This is the part where you run the code
def running(Result):
	count = 0
	#This is to load the operator Permutation
	for m in range(len(opList)):
		f = open("a.txt", 'r')

		#list 1 is the permutation of the operators (one of the Cartesian Products)
		list1= opList[m]

		#This part is to load the file
		for k in f:
			k.rstrip('/n')
			for m in range(len(numlist)):
				#replace the stuff in the file (num1, num2,...) with the actual number from number list
				k=k.replace(num[m], numlist[m])
			#This is to replace the first 4 operators
			for n in range(len(list1)):
				k=k.replace("op", list1[n], 1)
			#This is to replace the last operat
			#laststring = "%s" %list1[4]
			#k=k.replace("op", laststring, 1)
			if round(Cal(k), 3) == round(float(Result),3):
				#stop all program after the first exprsesion is found
				print k
				return k
				break 
		count +=1
		print count
		f.close()
## Run the code by printing the function 
print running(890.000)


