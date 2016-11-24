from multiprocessing import Pool
from rpn import RPN
import logging

logging.basicConfig(format = u'[%(asctime)s]  %(message)s', level = logging.DEBUG)

def calculate(arr):
	for i in range(len(arr)):
		try:
			int(arr[i])
		except:
			if (arr[i] == "+"):
				arr[i] = arr[i-2]+arr[i-1]
				break
			elif (arr[i] == "-"):
				arr[i] = arr[i-2]-arr[i-1]
				break
			elif (arr[i] == "*"):
				arr[i] = arr[i-2]*arr[i-1]
				break
			elif (arr[i] == "/"):
				try:
					arr[i] = arr[i-2]/arr[i-1]
					break
				except:
					return False
	arr.pop(i-1)
	arr.pop(i-2)
	if (len(arr) == 1):
		return arr[0]
	else:
		return calculate(arr)

if __name__ == '__main__':
	print("Введи в меня выражение, или вызови из файла. Прим.: 'file test.txt'")
	while True:
		r = input("> ")
		if(r[:4] != "file"):
				print('=', calculate(RPN(r)) )
		else:
			logging.debug("Opening the file...")
			try: 
				f = open(r[5:])
			except Exception as e:
				print("Ошибка чтения файла")
			else:
					p = Pool(processes=4) # Тщетные попытки многопоточности
					lines = []
					answers = []
					logging.debug("Pushing the array...")
					for line in f:
						line = line.replace("\n", "")
						lines.append(line)
					logging.debug("Start calculating!")
					answers = p.map(RPN, lines)
					answers = p.map(calculate, answers)
					p.close()
					p.join()
					logging.debug("Finish calculating!")
					for i in range(len(answers)):
						print("{:4}.".format(i+1), lines[i], " = ", answers[i])
