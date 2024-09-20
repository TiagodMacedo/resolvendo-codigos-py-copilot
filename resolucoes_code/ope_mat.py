# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

num1 = int(input("Digite o primeiro numero:"))
num2 = int(input("Digite o segundo numero:"))

operacao = input("Digite a operação que deseja realizar (+, -, *, /):")

if operacao == "+":
    print(num1 + num2)
elif operacao == "-":
    print(num1 - num2)
elif operacao == "*":
    print(num1 * num2)
elif operacao == "/":
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Não é possível dividir por zero")
else:
    print("Operação inválida")