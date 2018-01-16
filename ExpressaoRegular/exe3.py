import re
#comparando CEP com expressão regular
#cep = re.compile('d{5}-d{3}')
#result = cep.match('89000-000')
result = re.match('\d{5}-\d{3}','89900-000')
print(result.group()) #printa "89900-000"

#comparando placas de veículos com expressão regular
placa = re.match('([a-z]{3}|[A-Z]{3})-\d{4}','AAA-1234')
print(placa.group()) #retorna "AAA-1234"
print(placa)
