# Recebe a entrada do usuário (valor e prioridade)
entrada = input().strip()
valor_str, prioridade = entrada.split()
valor = int(valor_str)

def decisao(valor, prioridade):
  if valor > 1000 and prioridade == "alta":
    return "revisao"
  elif valor <=1000 and (prioridade == "alta" or prioridade == "media"):
    return "aprovado"
  else:
    return "rejeitado"
  
resultado = decisao(valor, prioridade)
print(resultado)