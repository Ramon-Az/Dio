entrada = input()
nomes_transformados = [nome.strip().upper() for nome in entrada.split(',')]
print('; '.join(nomes_transformados))
