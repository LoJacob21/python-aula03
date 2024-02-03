#Crie um progra,a que mostre a tabuada do numero 2,
#usando o laço de repetição while.

#Agora altere o código para solicitar a tabuada ao usuario

print("TABUADAS")
tabuada = int(input("Escolha um número para fazer a tabuada: "))

contador = 0
while (contador <= 10):
    print(f"{tabuada} x {contador} = {contador*tabuada}")
    contador += 1 