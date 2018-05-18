fita1 = [' ']
fita2 = [' ']
fita3 = [' ']
cont1 = 0
cont2 = 0


def entrada():
	fita_entrada = input()
	return fita_entrada

def q0(fita_entrada,inicio,fim):
	aux = fita_entrada[inicio:fim]
	for i in range(len(aux)):
		fita1.append(aux[i])
	global cont1
	cont1 = len(fita1)-1
	

def q1(fita_entrada,inicio,fim):
	aux = fita_entrada[inicio:fim]
	for i in range(len(aux)):
		fita2.append(aux[i])
	global cont2
	cont2 = len(fita2)-1
def q4():
	global cont1
	global cont2
	global fita3
	if((fita1[cont1] == '0' and fita2[cont2] == '0') or (fita1[cont1] == '1' and fita2[cont2]== '0') or (fita1[cont1] == '0' and fita2[cont2] == '1')):
		fita3.append(1)
		cont1 = cont1-1
		cont2 = cont2-1
		q3()
	elif(fita1[cont1] == '1' and fita2[cont2] == '1'):
		fita3.append(0)
		cont1 = cont1 -1
		cont2 = cont2-1
		q4()
	elif(fita1[cont1] == ' ' and fita2[cont2] == ' '):
		fita3.append(1)
		q3()
def q5():
	#print(fita3,"ACEITA")
	global fita3
	msg = ""
	for i in range(1,len(fita3)):
		msg = msg+str(fita3[i])
	#print(fita3)
	print(msg[::-1],"ACEITA")

def q3():
	global cont1
	global cont2
	global fita3
	if(len(fita1) == len(fita2)): #fitas de tamanho igual
		if((fita1[cont1] == '0' and fita2[cont2] == '0') or (fita1[cont1] == '1' and fita2[cont2] == '0') or (fita1[cont1] == '0' and fita2[cont2] == '1') ):
			fita3.append('0')
			cont1 = cont1-1
			cont2 = cont2-1
			return q3()
		elif(fita1[cont1] == '1' and fita2[cont2] == '1'):
			fita3.append('0')
			cont1 = cont1-1
			cont2 = cont2-1
			return q4()

		return q5()
	'''elif(len(fita1) != len(fita2)):
		#print("entrou")
		#print(cont1)
		#print(cont2)
		if(len(fita1) > len(fita2)):
			if((fita1[cont1] == '0' and fita2[cont2] == '0') or (fita1[cont1] == '1' and fita2[cont2] == '0') or (fita1[cont1] == '0' and fita2[cont2] == '1') ):
				fita3.append('0')
				cont1 = cont1-1
				cont2 = cont2-1
				return q3()
			elif(fita1[cont1] == '1' and fita2[cont2] == '1'):
				fita3.append('0')
				cont1 = cont1-1
				cont2 = cont2-1
				return q4()
			else:
				for i in range(cont1):
					#print(fita3[i])
					fita3.append(fita1[i])
				return q5()
		'''

def inicializa_fita(fita_entrada):
	indice = 0
	saida = False
	for i in range(len(fita_entrada)):
		if(fita_entrada[i] == '+'):
			indice = i
			saida = True

	if(saida == False):
		print(fita_entrada,"REJEITA")
	else:
		q0(fita_entrada,0,indice)
		fita1.append(' ') #adiciona um espaço em branco ao final da lista
		q1(fita_entrada,indice+1,len(fita_entrada))
		fita2.append(' ') #adiciona um espaço em branco ao final da lista
		#print(fita1)
		#print(fita2)
		q3()

entrada =entrada()
inicializa_fita(entrada)
