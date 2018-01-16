import re

text = 'Aplicacoes de text mining versao 1'
print(re.match(r'(.*) text',text).group()) #o .group() devolve um objeto

email = 'Nosso e-mail e jailson.pereira@uea.com.br'
print(re.search(r'([\w.-]+)@([\w.-]+)',email).group()) #retorna o email inteiro
print(re.search(r'([\w.-]+)@([\w.-]+)',email).group(1)) #retorna o username
print(re.search(r'([\w.-]+)@([\w.-]+)',email).group(2))#retorna o host


#uso do split
text = """Ross McFluff: 834.345.1254 155 Elm Street"""
entries = re.split("\n+",text)
entries = [re.split(":? ",entry,4)for entry in entries]
print(entries)
