# And, Or ou Not
from sentry_sdk.integrations.logging import SentryHandler

# Lógica E / And

verifica_email = True
verifica_senha = False

verifica_login = verifica_email and verifica_senha

print('Login E Senha')
print(verifica_login)


# Lógica Ou / Or
verifica_email = True
verifica_senha = True

verifica_login = verifica_email or verifica_senha

print('Login OU Senha')
print(verifica_login)

# Lógica Não / Not
print('Lógica not'')
negacao = not True
print(negacao)

if not verifica_login:
    print('logue novamente')
else:
    print('entra no programa')

