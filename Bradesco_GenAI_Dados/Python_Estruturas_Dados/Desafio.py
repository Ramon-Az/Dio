def calcular_imposto(salario):
    aliquota = 0.00
    if (salario >= 0 and salario <= 1100):
        aliquota = 0.05
    elif(salario >= 1100.01 and salario <= 2500.00):
        aliquota = 0.10 
    else:
        aliquota = 0.15
    
    return aliquota * salario

valor_salario = float(input("Digite o valor do salário: R$ "))
valor_beneficio = float(input("Digite o valor do benefício: R$ "))

valor_imposto = calcular_imposto(valor_salario)
resultado = (valor_salario - valor_imposto) + valor_beneficio

print(f"O valor do imposto: R$ {valor_imposto:.2f}\nO Salário, descontado os impostos {resultado:.2f}")
