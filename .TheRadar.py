# coding=utf-8

print "\n*******************************************************************"  # Tributo ao TheHarvester
print "*                                                                 *"
print "* _______ _          _____           _                            *"
print "*|__   __| |        |  __ \         | |                           *"
print "*   | |  | |__   ___| |__) |__ _  __| | __ _ _ __                 *"
print "*   | |  | '_ \ / _ \  _  // _` |/ _` |/ _` | '__|                *"
print "*   | |  | | | |  __/ | \ \ (_| | (_| | (_| | |                   *"
print "*   |_|  |_| |_|\___|_|  \_\__,_|\__,_|\__,_|_|                   *"
print "*                                                                 *"
print "* TheRadar Ver. 0.9                                               *"
print "* Coded by Doctor Beakman                                         *"
print "* Railroad University of Paranapiacaba                            *"
print "* beakman@ufp.edu.com                                             *"
print "*                                                                 *"
print "*******************************************************************\n"

# 1 Configuração do Menu
AnoA = ['2009: Local: Vítimas.\n']
def menu():
    print("\tMENU\n")
    print("\t1 - Escanear")
    print("\t2 - Sobre")
    print("\t3 - Sair\n")
    selection = int(input("Digite o número do menu que deseja acessar: "))
    print ("\n")

    if selection == 1:
        escanear()
    elif selection == 2:
        sobre()
        menu()
    elif selection == 2009:
        print(AnoA[0])

    elif selection == 3:
        exit
    else:
        print("Escolha inválida, tente novamente.\n")
        menu()

# 2 Configuração do Scan criada por Adriel Freud
def escanear():
    import time

    raw_input("ENTER para confirmar o processo. ")

    print("\n\t1%")
    time.sleep(1)
    print("\t6%")
    time.sleep(2)
    print("\t15%")
    time.sleep(3)
    print("\t22%")
    time.sleep(1)
    print("\t35%")
    time.sleep(3)
    print("\t50%")
    print("\t65%")
    time.sleep(3)
    print("\t80%")
    time.sleep(4)
    print("\t91%")
    print("\t100%\n\nPesquisa Concluida!\n")
    time.sleep(1)
    print ("Processando dados por ano")
    time.sleep(1)
    print ("\tResultados:\n")
    print("\tA - 2009")
    print("\tB - 2010")
    print("\tC - 2011")
    print("\tD - 2012")
    print("\tE - 2013")
    print("\tF - 2014")
    print("\tG - 2015")
    print("\tH - 2016")
    print("\tI - 2017\n")

# Segundo Menu
    selection = int(input("Digite o ano que deseja acessar: "))
    print ("\n")

    if selection == 2009:
        print(AnoA[0])

    else:
        print("Escolha inválida, reinicie o programa.\n")
        menu()

def sobre():
    print("Sobre: Este programa foi desenvolvido em python.\n")

print menu()
