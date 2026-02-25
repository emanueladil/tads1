# Cálculo de salário
funcionarioNome = input("Digite o nome do funcionário: ")
salarioFixo = float(input("Digite o valor do salário fixo: "))
vendas = float(input("Digite o valor vendido durante o mês: "))

salarioReceber = (salarioFixo + vendas * 0.15)

print(f"{funcionarioNome} receberá R${salarioReceber:.2f}")
