import re

message = "Olá meu nome é João e meu telefone é (11) 99999-9999"
phone_num_regex = re.compile(r' \(\d\d\) \d\d\d\d\d-\d\d\d\d')

try:
    mo = phone_num_regex.search(message) # mo = match object procura na string se tem algo do tipo do regex
    print(mo.group()) # group() retorna o que foi encontrado ou causa erro

except AttributeError:
    print("Não encontrado nenhum númeor de celular")

