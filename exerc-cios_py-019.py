# Lista de vendas brutas dos vendedores
vendas_brutas = []

while True:
    i = float(input("Insira a venda bruta de cada vendedor(Digite [0] para encerrar: "))
    if i == 0 :
        break
    else:
        vendas_brutas.append(i)

# Inicializando um array de contadores com zeros para cada intervalo
contadores = [0] * len(vendas_brutas)

# Calculando os salários e incrementando os contadores
for venda_bruta in vendas_brutas:
    salario = 200 + 0.09 * venda_bruta

    if salario >= 200 and salario <= 299:
        contadores[0] += 1
    elif salario >= 300 and salario <= 399:
        contadores[1] += 1
    elif salario >= 400 and salario <= 499:
        contadores[2] += 1
    elif salario >= 500 and salario <= 599:
        contadores[3] += 1
    elif salario >= 600 and salario <= 699:
        contadores[4] += 1
    elif salario >= 700 and salario <= 799:
        contadores[5] += 1
    elif salario >= 800 and salario <= 899:
        contadores[6] += 1
    elif salario >= 900 and salario <= 999:
        contadores[7] += 1
    else:
        contadores[8] += 1

# Exibindo os resultados
intervalos = ["$200 - $299", "$300 - $399", "$400 - $499", "$500 - $599", "$600 - $699", "$700 - $799", "$800 - $899", "$900 - $999", "$1000 em diante"]

for i in range(len(contadores)):
    print(f"Vendedores no intervalo {intervalos[i]}: {contadores[i]}")
