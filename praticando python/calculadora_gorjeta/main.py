valor_conta = float(input("Digite o valor da sua conta: "))
porcentagem_gorjeta = float(input("Qual a porcentagem que você gostaria de dar de gorjeta? "))

gorjeta = (porcentagem_gorjeta / 100) * valor_conta 
valor_final = valor_conta + gorjeta
print(valor_final)