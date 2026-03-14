# Leitura da linha de entrada
entrada = input().strip()

# TODO: Separe os campos da entrada e calcule o valor total da venda (quantidade * valor unitário)
# Dica: Use split(',') para separar os valores e int() para converter para inteiro
produto, quantidade, valor_unitario = entrada.split(',')
total = int(quantidade) * int(valor_unitario)

print(f"{produto}: {total}")  # Exemplo de saída formatada