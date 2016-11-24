import re
def exInt(k):
	try:
		k = int(k)
	except:
		try:
			k = int(k[1:-1])
		except:
			return False
	return k

def get_first_level(r):
	t = ""
	a = []
	saving = False
	depth = 0
	for ch in r:
		if ch == ")": #встретили закрывающуюся
			depth-=1 #отналяи глубины
			if depth < 0: #закрыли внешний уровень
				saving = False
				if (t):
					a.append(t)
				depth = 0
				t = ""

		t += ch if saving else ""

		if ch == "(": #Открыли скобку
			if (saving): #Если уже открыта скобка была, то это другой уровень
				depth+=1
			saving = True		

	return a

while True:
	r = input("> ")
	t = re.findall(r"(\d+\.\d+)|\((\-\d+)\)|(\d+)|\((\-\d+\.\d+)\)", r)
	result = []
	for i in t:
		for j in i:
			if len(j):
				try:
					result.append(float(j))
				except:
					pass

	#t = t.group(0)
	print(result)