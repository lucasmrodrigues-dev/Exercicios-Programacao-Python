# Escreva um programa que leia um valor em metros e o exiba convertido em milímetros.
metros = float(input("Digite o valor em métros: ")) 
milímetros = metros * 1000 
print("%10.3f metros equivalem a %10.3f milímetros." % (metros, milímetros))