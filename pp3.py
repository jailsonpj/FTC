fita1 = [' ']
fita2 = [' ']
fita3 = [' ']
fita4 = [' ']
fita_entrada = ' '
cont1 = 0
cont2 = 0
cont3 = 0


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

def q5():
	
	global fita3
	global fita_entrada
	msg = ""
	for i in range(1,len(fita3)):
		msg = msg+str(fita3[i])
	
	print(fita_entrada+"="+msg[::-1],"ACEITA")

def q4():
	global cont1
	global cont2
	global fita3
	global fita4
	global cont3
	if((fita1[cont1] == '0' and fita2[cont2] == '0' and fita4[cont3] == '1')):
		fita3.append('1')
		fita4.append('1')
		cont1 = cont1-1
		cont2 = cont2-1
		cont3 = cont3+1
		return q3()
	elif((fita1[cont1] == '1' and fita2[cont2]== '0' and fita4[cont3] == '1') or (fita1[cont1] == '0' and fita2[cont2] == '1' and fita4[cont3]=='1')):
		fita3.append('0')
		fita4.append('1')
		cont1 = cont1-1
		cont2 = cont2-1
		cont3 = cont3+1
		return q4()
	elif(fita1[cont1] == '1' and fita2[cont2] == '1' and fita4[cont3] == '1'):
		fita3.append('1')
		fita4.append('1')
		cont1 = cont1 -1
		cont2 = cont2-1
		cont3 = cont3+1
		return q4()
	elif(fita1[cont1] == ' ' and fita2[cont2] == ' '):
		fita3.append('1')
		#print("entrou")
		return q3()
	
	elif((fita1[cont1]=='1' and fita2[cont2]==' ' and fita4[cont3]=='1')):
		fita3.append('0')
		#fita3.append('1')
		cont1=cont1-1
		return q4()

	elif(fita1[cont1]=='0' and fita2[cont2]==' ' and fita4[cont3]=='1'):
		fita3.append('1')
		cont1=cont1-1
		return q3()

	elif(fita2[cont2]=='1' and fita1[cont1]==' ' and fita4[cont3]=='1'):
		fita3.append('0')
		#fita3.append('1')
		#fita4.append(' ')
		cont2=cont2-1
		return q4()

	elif(fita2[cont2]=='0' and fita1[cont1]==' ' and fita4[cont3]=='1'):
		fita3.append('1')
		cont2=cont2-1
		return q3()

	elif((fita2[cont2]=='1' and fita1[cont1]==' ') or (fita2[cont2]=='0' and fita1[cont1]==' ')):
		fita3.append(fita2[cont2])
		cont2=cont2-1
		return q3()
	
	elif((fita1[cont1]=='1' and fita2[cont2]==' ') or (fita1[cont1]=='0' and fita2[cont2]==' ')):
		fita3.append(fita1[cont1])
		cont1=cont1-1
		return q3()

def q3():
	global cont1
	global cont2
	global cont3
	global fita3
	global fita4

	#print(fita3)
	if(len(fita1) == len(fita2)): #fitas de tamanho igual
		if((fita1[cont1] == '0' and fita2[cont2] == '0')):
			fita3.append('0')
			cont1 = cont1-1
			cont2 = cont2-1
			return q3()
		elif((fita1[cont1] == '1' and fita2[cont2] == '0') or (fita1[cont1] == '0' and fita2[cont2] == '1') ):
			fita3.append('1')
			cont1 = cont1-1
			cont2 = cont2-1
			return q3()
		elif(fita1[cont1] == '1' and fita2[cont2] == '1'):
			fita3.append('0')
			fita4.append('1') #Fita para guardar os numeros cujo o valor 1 sobe
			cont1 = cont1-1
			cont2 = cont2-1
			cont3 = cont3+1
			return q4()
		else:
			return q5()
	else:#fitas de tamanhos diferentes
		if(fita1[cont1]=='0' and fita2[cont2]=='0'):
			fita3.append('0')
			cont1 = cont1-1
			cont2 = cont2-1
			return q3()
		elif((fita1[cont1]=='0' and fita2[cont2]=='1') or (fita1[cont1]=='1' and fita2[cont2]=='0')):
			fita3.append('1')
			cont1=cont1-1
			cont2=cont2-1
			return q3()
		elif((fita1[cont1]=='1' and fita2[cont2]=='1')):
			fita3.append('0')
			fita4.append('1')
			cont1 = cont1-1
			cont2 = cont2-1
			cont3 = cont3+1
			return q4()
		elif((fita1[cont1]=='1' and fita2[cont2]==' ') or (fita1[cont1]=='0' and fita2[cont2]==' ')):
			fita3.append(fita1[cont1])
			cont1=cont1-1
			return q3()
		elif((fita2[cont2]=='1' and fita1[cont1]==' ') or (fita2[cont2]=='0' and fita1[cont1]==' ')):
			fita3.append(fita2[cont2])
			cont2=cont2-1
			return q3()
		else:
			return q5()
				
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
		q3()

entrada =entrada()
fita_entrada = entrada
#print(entrada)
inicializa_fita(entrada)
#global fita_entrada

