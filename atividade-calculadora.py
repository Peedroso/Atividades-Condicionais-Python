
import os 

#limpando a tela 
os.system("cls")

print('''  
███████████████████████████████████████████████████████████████████
█─▄▄▄─██▀▄─██▄─▄███─▄▄▄─█▄─██─▄█▄─▄████▀▄─██▄─▄▄▀█─▄▄─█▄─▄▄▀██▀▄─██
█─███▀██─▀─███─██▀█─███▀██─██─███─██▀██─▀─███─██─█─██─██─▄─▄██─▀─██
▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▀▄▄▄▄▀▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀  ''')

#entrada
n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))
operação = input("Digite a operação")

if(operação == "+"):
 resultado = n1 + n2
 print("Sera feito soma de dois valores")

elif(operação == "-"):
 resultado = n1 - n2
 print("Sera feito a subtração de dois valores")

elif(operação == "/"):
 resultado = n1 / n2 
 print("Sera feito a divisão de dois valores")

elif(operação == "*"):
 resultado = n1 * n2 
 print("Sera feito multiplicação dos dois numeros")

#saida
print("O resultado foi:", resultado)
print("A operação foi:", operação)

