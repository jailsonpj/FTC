import re

def modifica_padrao(cpf):#pega os primeiros 9 digitos para a validação
    padrao = re.compile(r'[0-9]')
    lista = re.findall(padrao,cpf)
    return lista

def conta_dig(cpf_novo,peso):#faz a validação dos digitos conforme os pesos
    soma = 0
    for i in range(0,len(peso)):
        soma = (peso[i]*int(cpf_novo[i])) + soma
    if(soma%11 < 2):
        digito = 0
    elif(soma%11 >= 2):
        digito = 11 - (soma%11)
    return digito

def valida_cpf(cpf):
    padrao = re.compile(r'[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}$') #valida quantidade de numeros
    if(re.match(padrao,cpf)):
        cpf_novo = modifica_padrao(cpf)

        peso = [10,9,8,7,6,5,4,3,2]
        primeiro = conta_dig(cpf_novo,peso)
        peso.insert(0,11) #inserir para fazer a validação dos dois ultimos digitos
        segundo = conta_dig(cpf_novo,peso)
        if(int(cpf_novo[len(cpf_novo)-2]) == primeiro and int(cpf_novo[len(cpf_novo)-1]) == segundo ):
            return True
        else:
            return False
    else:
        return False

def valida_cnpj(cnpj):
    padrao = re.compile(r'[0-9]{2}\.[0-9]{3}\.[0-9]{3}/[0-9]{4}-[0-9]{2}$')
    if(re.match(padrao,cnpj)):
        cnpj_novo = modifica_padrao(cnpj)

        peso = [5,4,3,2,9,8,7,6,5,4,3,2]
        primeiro = conta_dig(cnpj_novo,peso)
        peso.insert(0,6)
        segundo = conta_dig(cnpj_novo,peso)

        if(int(cnpj_novo[len(cnpj_novo)-2]) == primeiro and int(cnpj_novo[len(cnpj_novo)-1]) == segundo ):
            return True
        else:
            return False
    else:
        return False

def valida_data(data):
    padrao = re.compile(r'[0-9]{4}\.[0-9]{2}\.[0-9]{2}$')
    if(re.match(padrao,data)):
        lista = data.split('.')
        ano = int(lista[0])
        mes = int(lista[1])
        dia = int(lista[2])
        if(ano > 0 and ano <= 2018 ):
            if(mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
                if(dia >=1 and dia <= 31):
                    return True
                else:
                    return False

            if(mes == 4 or mes == 6 or mes == 9 or mes == 1):
                if(dia >=1 and dia <= 30):
                    return True
                else:
                    return False

            if(mes == 2):
                if(ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0):
                    if(dia >= 1 and dia <= 29):
                        return True
                    else:
                        return False
                else:
                    if(dia >= 1 and dia <= 28):
                        return True
                    else:
                        return False
            else:
                return False
        else:
            return False
    else:
        return False

def valida_horas(horas):
    padrao = re.compile(r'[0-9]{2}:[0-9]{2}:[0-9]{2}$')
    if(re.match(padrao,horas)):
        lista = horas.split(':')
        hora = int(lista[0])
        minutos = int(lista[1])
        segundos = int(lista[2])

        if( (hora >= 0 and hora <= 24) and (minutos >= 0 and minutos <= 60 ) and (segundos >= 0 and segundos <= 60) ):
            return True
        else:
            return False
    else:
        return False

def valida_preco(preco):
    padrao = re.compile(r'\[[0-9]*\.[0-9]{2},[0-9]*\.[0-9]{2}\]$')
    if(re.match(padrao,preco)):
        return True
    else:
        return False

def padrao_cod_num(codigo):
    padrao = re.compile(r'[0-9]{9}$')
    if(re.match(padrao,codigo)):
        return True
    else:
        return False

def padrao_cod_letranum(codigo):
    padrao = re.compile(r'[a-z0-9]{5}$')
    if(re.match(padrao,codigo)):
        return True
    else:
        return False

def padrao_num_par(codigo):
    padrao = re.compile(r'[0-9]*[02468]{3}$')
    if(re.match(padrao,codigo)):
        return True
    else:
        return False

def padrao_num_binario(codigo):
    padrao = re.compile(r'[0-9]*[01]{3}$')
    if(re.match(padrao,codigo)):
        return True
    else:
        return False


def validar_codigo(codigo):
    lista = codigo.split('-')
    valido = []
    if(len(lista)<3 or len(lista)>4):
        return False
    if(len(lista) == 3):
        valido.append(padrao_cod_num(lista[0]))
        valido.append(padrao_cod_letranum(lista[1]))
        valido.append(padrao_num_par(lista[2]))

        if(valido[0] == True and valido[1] ==  True and valido[2] == True):
            return True
        else:
            return False
    if(len(lista) == 4):
        valido.append(padrao_cod_num(lista[0]))
        valido.append(padrao_cod_letranum(lista[1]))
        valido.append(padrao_num_par(lista[2]))
        valido.append(padrao_num_binario(lista[3]))

        if(valido[0] == True and valido[1] ==  True and valido[2] == True and valido[3]):
            return True
        else:
            return False


def processamento(entrada):
    lista = entrada.split(' ')
    saida = []
    flag = True
    if(len(lista)<6 or len(lista) > 6):
        return False

    saida.append(valida_cpf(lista[0]))
    saida.append(valida_cnpj(lista[1]))
    saida.append(valida_data(lista[2]))
    saida.append(valida_horas(lista[3]))
    saida.append(valida_preco(lista[4]))
    saida.append(validar_codigo(lista[5]))
    for i in range(6):
        if(saida[i] != True):
            flag = False
    return flag

try:
    entrada = input()
    print(processamento(entrada))
except(EOFError):
    print(True)
