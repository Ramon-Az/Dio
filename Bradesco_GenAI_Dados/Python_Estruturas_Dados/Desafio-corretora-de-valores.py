# Lê a linha de entrada e separa os valores
entrada = input()
abertura_str, fechamento_str = entrada.split()

# Converte os valores para inteiros
abertura = int(abertura_str)
fechamento = int(fechamento_str)

# TODO: Compare os valores de abertura e fechamento e imprima o resultado correto ("ALTA", "BAIXA" ou "ESTAVEL")
if fechamento > abertura:
    print("ALTA")
elif fechamento < abertura:
    print("BAIXA")
else:
    print("ESTAVEL")