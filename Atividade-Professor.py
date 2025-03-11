
import os 

#limpando a tela 
os.system("cls")

print('''     
█▀█ █▀█ █▀█ █▀▀ █▀▀ █▀ █▀ █▀█ █▀█
█▀▀ █▀▄ █▄█ █▀░ ██▄ ▄█ ▄█ █▄█ █▀▄         ''')


nome = input("Digite seu nome: ")
quantidade = int(input("Digite a quantidade de aulas: "))
nivel = input("Digite o seu nivel")

nivel01 = 12.00
nivel02 = 17.00
nivel03 = 25.00

salario = quantidade * nivel

if (nivel01):
    salario = 12.00 * quantidade *4
    
    
elif(nivel02):
    salário = 17.00 * quantidade *4
  

else: (nivel03)
salário = 25.00 * quantidade *4

print("O resultado do salario é: ", salario)




