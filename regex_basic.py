import re

message = "Olá meu nome é João e meu telefone é (11) 99999-9999 mas atendo no (11) 88888-8888 também"
phone_num_regex = re.compile(r' \((\d\d)\) (\d\d\d\d\d-\d\d\d\d)') # Colocando parenteses criamos grupos

try:
    mo = phone_num_regex.search(message) # mo = match object procura na string se tem algo do tipo do regex
    mo2 = phone_num_regex.findall(message) # retorna uma lista com todos os resultados encontrados
    print(mo.group()) # group() retorna o que foi encontrado ou causa erro
    print(f" o DD do primeiro número é {mo.group(1)} e número é {mo.group(2)}") # retorna o primeiro grupo, estamos ().
    print(mo2)

except AttributeError:
    print("Não encontrado nenhum númeor de celular")

# Para criar prefixos
bat_regex = re.compile(r'Bat(man|mobile|copter|bat)') # | é o operador OR
mo = bat_regex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1)) # retorna o primeiro grupo encontrado