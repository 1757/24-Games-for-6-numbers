import itertools
from ReversePolish import Cal



### Generation of cartesian products (permutation with replacement, without ) of operators:
def cartProd(number, list):
	permList=[]
	for x in itertools.product(list, repeat= number):
		permList.append(x)
	return permList

## Pattern Generation: 
toPerm = ['num1', 'num2', 'num3', 'num4', 'num5', 'num6', 'op1', 'op2', 'op3', 'op4', 'op5']
toPerm1 = ['num1', 'num2', 'num3', 'num4', 'num5', 'num6', 'op', 'op', 'op', 'op', 'op']

# objectOfperm = itertools.permutations(toPerm, 11)
# file= open("Combifile.txt", 'w')
# for x in objectOfperm:
# 	y = ' '.join(str(z) for z in x)
# 	file.write('%s\n' %y)


class unique_element:
	def __init__(self,value,occurrences):
		self.value = value
		self.occurrences = occurrences

def perm_unique(elements):
	eset=set(elements)
	listunique = [unique_element(i,elements.count(i)) for i in eset]
	u=len(elements)
	return perm_unique_helper(listunique,[0]*u,u-1)

def perm_unique_helper(listunique,result_list,d):
	if d < 0:
		yield tuple(result_list)
	else:
		for i in listunique:
			if i.occurrences > 0:
				result_list[d]=i.value
				i.occurrences-=1
				for g in  perm_unique_helper(listunique,result_list,d-1):
					yield g
				i.occurrences+=1

a = perm_unique(toPerm1)

file1 = open("x.txt", "w")
count =0
for x in a:
	if x[0] != 'op' and x[1] != 'op' and x[10] == 'op':
		y = ' '.join(str(z) for z in x)
		k=y
		num = ["num1", "num2", "num3", "num4", "num5", "num6"]
		numlist = ["1", "1", "1", "1", "1", "1"]
		list1 = ("+", "+", "+", "+", "+")
		for m in range(len(numlist)):
			#replace the stuff in the file (num1, num2,...) with the actual number from number list
			k=k.replace(num[m], numlist[m])
		#This is to replace the first 4 operators
		k=k.replace("op", list1[1], 5)
		k=k+" "
		print k
		#This is to replace the last operat
		#laststring = "%s" %list1[4]
		#k=k.replace("op", laststring, 1)
		if Cal(k)== None:
			continue
		else:
			file1.write('%s\n' %y)
		count +=1
print count
