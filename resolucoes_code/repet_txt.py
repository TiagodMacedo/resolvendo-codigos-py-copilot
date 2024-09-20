# Vamos solicitar uma string e um numero inteiro como entrada. Depois teremos que retornar a string repetida o numero de vezes informado.

def repetir_string():
    string = input("Digite uma string: ")
    num_repeticoes = int(input("Digite o número de repetições: "))
    return (' '.join([string] * num_repeticoes))

print(repetir_string())
