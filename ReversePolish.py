
# numberlist=[1, 2, 3, 4]
# operatorlist=["+", "-", "*", "/"]


#The code used to evaluate a reverse polish notation, with syntax: "num num op op " (there's a space at the end)
def Cal(expression):
	""" Evaluate a reverse polish notation """
	#remove the last string thing in the expression (It's a preference, cos I generated the files such that there will be a white space at the end of each expression)
	expression = expression[:-1]
	stack = []
	try:
		for val in expression.split(' '):
			#if the expression is an operator, take the last 2 number from the stack and use the operator on them 
			if val in ['-', '+', '*', '/']:
					op1 = float(stack.pop())
					op2 = float(stack.pop())
					if val=='-': result = op2 - op1
					if val=='+': result = op2 + op1
					if val=='*': result = op2 * op1
					if val=='/': result = op2 / op1
					stack.append(result)
			else:
					#if the expression is a number, add to the stack
					stack.append(float(val))
		#the last number in the stack will be the result of the reverse polish calculation
		return stack.pop()
	except:
		#if the expression is incorrect (or things like divide by 0), return None
		return 0.0
#print Cal("6 6 + 1 25 / - 75 * 7 - ") 


