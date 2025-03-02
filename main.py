from os import system, name
from time import sleep

def cls():
    system("cls") if name == 'nt' else system('clear')
cls()

def menu():
    while True:
        try:
            print("==== CONVERSOR ====\n")
            print("[1] Converter decimal para binário\n[2] Converter binário para decimal\n[3] Converter Texto para binário\n[4] Converter binário para texto\n[5] Sair")

            entrada = int(input("Digite: "))
            
            opcoes = {
                1: decimalparabinario,
                2: binarioparadecimal, 
                3: textoparabinario,
                4: binarioparatexto,
                5: exit
            }
            
            if entrada in opcoes:
                opcoes[entrada]()
            else:
                print("Erro, escolha um número válido")
                sleep(2)
                cls()
        except ValueError:
            print("Erro, escolha apenas números válidos")
            sleep(2)
            cls()

def decimalparabinario():
    decimal = int(input("Número: "))
    binario = bin(decimal)[2:]
    print("Binário: ", binario)

    system('pause')

def binarioparadecimal(): 
    binario = input("Binário: ")
    decimal = int(binario, 2)
    print("Número: ", decimal)

    system('pause')

def textoparabinario():
    texto = input("Texto: ")
    binario = ''.join([format(ord(c), '08b') for c in texto])
    print("Binário: ", binario)
    
    system('pause')

def binarioparatexto():
    binario = input("Binário: ")
    texto = ''.join([chr(int(binario[i:i+8],2)) for i in range(0, len(binario), 8)])
    print("Texto: ", texto)

    system('pause')
    
menu()
