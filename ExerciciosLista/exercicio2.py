# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

lista = [1,2,3,4,5,6,7,8,9,10]
count = 0

for i in lista:
    count -= 1
    print(lista[count])

for i in reversed(lista):
    print(i)