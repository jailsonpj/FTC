
def entrada_estados(x):
	qnt_estados = int(x[0])
	return qnt_estados

def entrada_inicio(x):
	inicio = int(x[0])
	return inicio

def entrada_final(x):
	lista = []
	valor = x[1].split(']')
	padrao = valor[0].split(',')
	for i in range(len(padrao)):
		lista.append(int(padrao[i]))
	return lista

def entrada_delta(x):
	esquema = x[0]
	delta = eval(esquema)
	#print(len(delta))
	for i in range(len(delta)):
		delta[i].sort()
		#print(delta[i])
	
	return delta

def vetor_estado_inicial(estados,inicio):
	vetor_inicial = []
	
	for i in range(estados):
		coluna = []
		vetor_inicial.append(coluna)

	for i in range(estados):
		if(i == inicio):
			vetor_inicial[i].append(1)
		else:
			vetor_inicial[i].append(0)

	return vetor_inicial

def vetor_estado_aceitacao(estados,final):
	vetor_aceitacao = []
	for i in range(estados):
		vetor_aceitacao.append(0) 
	
	for i in range(len(final)):
		vetor_aceitacao[final[i]] = 1
	return vetor_aceitacao


def vetor_transicao_a(estados,matriz):
	lista = []
	matriz_transicao = []

	for i in range(estados):
		lista.append(matriz[i][0])

	#lista.sort()

	for i in range(estados): #matriz de funções de transição
		coluna = []
		matriz_transicao.append(coluna)
	
	for i in range(estados):
		for k in range(estados):
			if(lista[i] == k):
				matriz_transicao[i].append(1)
			else:
				matriz_transicao[i].append(0)


	return matriz_transicao
	#print(lista)
	#print(matriz_transicao)

def vetor_transicao_b(estados,matriz):
	lista = []
	matriz_transicao = []

	for i in range(estados):
		lista.append(matriz[i][1])

	#lista.sort()

	for i in range(estados): #matriz de funções de transição
		coluna = []
		matriz_transicao.append(coluna)
	
	for i in range(estados):
		for k in range(estados):
			if(lista[i] == k):
				matriz_transicao[i].append(1)
			else:
				matriz_transicao[i].append(0)

	return matriz_transicao

def trans_matriz(matriz):
	matriz_res = []
	for j in range(len(matriz[0])):
		linha = []
		for i in range(len(matriz)):
			linha.append(matriz[i][j])
		matriz_res.append(linha)
	return matriz_res

def multi_matriz(matriz_a,matriz_b):
	
	linha_a = len(matriz_a)
	coluna_a = len(matriz_a[0])
	matriz_res = []
	
	for i in range(linha_a):
		coluna = []
		matriz_res.append(coluna)
		
	for i in range(linha_a):
		for j in range(coluna_a):
			valor = 0
			for k in range(len(matriz_b[0])):
				valor = valor + (matriz_a[i][k] * matriz_b[k][j])
			matriz_res[i].append(valor)
	
	return matriz_res		

def mult_final(matriz_a,matriz_b):
	linha_a = len(matriz_a)
	coluna_a = len(matriz_a[0])

	for i in range(linha_a):
		for j in range(coluna_a):
			valor = 0
			for k in range(len(matriz_b)):
				valor = valor + (matriz_a[i][k] * matriz_b[k])
	return valor

def processamento(automato,palavra):
	
	inicial = vetor_estado_inicial(automato['estados'],automato['inicial'])
	aceitacao = vetor_estado_aceitacao(automato['estados'],automato['final'])
	
	resultado = trans_matriz(inicial)

	for i in range(len(palavra)):
		if(palavra[i] == 'a'):
			matriz_a = vetor_transicao_a(automato['estados'],automato['delta'])
			resultado = multi_matriz(resultado,matriz_a)
			#print(resultado)
		if(palavra[i] == 'b'):
			matriz_b = vetor_transicao_b(automato['estados'],automato['delta'])
			resultado = multi_matriz(resultado,matriz_b)
	
	saida = mult_final(resultado,aceitacao)
	if(saida == 1):
		print("ACEITA")
	else:
		print("REJEITA")
	

entrada = list(input().split(':'))

estados = entrada_estados(entrada[1].split(','))
inicio = entrada_inicio(entrada[2].split(','))
final = entrada_final(entrada[3].split('['))
delta = entrada_delta(entrada[4].split('}'))
#print(delta)
automato = {'estados':estados,'inicial':inicio,'final':final,'delta':delta}

quantidade_entrada = int(input())
for i in range(quantidade_entrada):
    palavra = input()
    processamento(automato,palavra)
