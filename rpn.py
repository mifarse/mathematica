def priority(x):  # returns piority level of char
	d = {"(": 0,
	 	 ")": 1, 
	 	 "+": 2, 
	 	 "-": 2, 
	 	 "*": 3, 
	 	 "/": 3}
	return d[x]

def RPN(expression):  # convert infix into postfix notation
	expression = expression.replace(" ", "")
	result = [] # результирующий массив
	stack = []  # стэк операций
	number = "" 
	for x in expression:
		try: # Нам на вход попало число?
			int(x)
		except: # Нет, значит это знак!
			if number:						# Если что-то в number накопилось,
				result.append(int(number))	# то мы закинем в результирующий массив
				number = ""					# и опустошим переменную.
			if(stack == [] or x == "("):
				stack.append(x)
			elif(x == ")"):
				stop = True
				while(stop): # Выгружаем стек до тех пор, пока не встретим "("
					poped = stack.pop()
					if(poped == "("):
						stop = False
					else:
						result.append(poped)
			else:
				for i in range(len(stack)): 				# Пробегаемся по стеку
					if(priority(stack[-1]) >= priority(x)): # Если приоритет верхнего элемента больше либо равен текущему,
						result.append(stack.pop())			# то убираем последний эл-т из стека, добавляя его в результирующий
				stack.append(x)
		else: 
			number+=x # Собираем число из цифр
	if number:
		stack.append(int(number))
	for i in range(len(stack)):
		result.append(stack.pop())
	return result