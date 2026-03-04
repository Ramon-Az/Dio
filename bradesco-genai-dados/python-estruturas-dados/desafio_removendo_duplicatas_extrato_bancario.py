""" Desafio
O Banco ByteSafe é conhecido por sua eficiência digital, mas recentemente um bug no sistema causou a duplicação de algumas transações em seu extrato online. Como analista de dados do banco, você foi encarregado de criar uma ferramenta que ajude a identificar e remover essas inconsistências. Cada linha do extrato é uma sequência de identificadores de transações, separados por espaço, e pode conter transações repetidas. Sua missão é garantir que cada transação apareça apenas uma vez, mantendo a ordem da primeira ocorrência. Assim, o extrato ficará limpo e sem duplicatas, facilitando a conferência dos clientes e a auditoria do banco.

Implemente uma função que receba uma string com identificadores de transações separados por espaço e retorne uma nova string, também separada por espaço, contendo apenas a primeira ocorrência de cada transação, na ordem em que aparecem originalmente. Não utilize bibliotecas externas para manipulação de listas ou conjuntos.
"""

# Leitura da linha de identificadores de transações
entrada = input()

# TODO: Crie uma lista com as transações sem duplicatas, mantendo a ordem da primeira ocorrência
# Dica: Percorra cada transação e adicione à lista apenas se ainda não estiver presente

def transacoes_unicas(entrada):
    transacoes = entrada.split()
    transacoes_vistas = []
    for transacao in transacoes:
        if transacao not in transacoes_vistas:
            transacoes_vistas.append(transacao)
    return transacoes_vistas

transacoes_unicas = transacoes_unicas(entrada)

print(' '.join(transacoes_unicas))  # Descomente após implementar a lógica