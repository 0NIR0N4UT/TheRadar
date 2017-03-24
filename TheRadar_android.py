#!/usr/bin/env python
# coding=utf-8

print " \n******************************"
print " *___    __  _  _  _  _  _    *"
print " * | |_||_  |_)|_|| \|_||_)   *"
print " * | | ||__ | \| ||_/| || \   *"
print " *                            *"
print " * TheRadar Ver. 0.99         *"
print " * Coded by:                  *"
print " * Dr. Adriano Casser         *"
print " * Railroad University of     *"
print " * Paranapiacaba              *"
print " * adriano.casser@ufp.edu.com *"
print " *                            *"
print " ******************************\n\n"

# 1 Configuração de Listas
AnoA = ['2009: Local: Vitimas.\n\n Obrigado pela consulta.\n\n END OF TRASMISSION']
AnoB = ['2010: Local: Vitimas.\n\n Obrigado pela consulta.\n\n END OF TRASMISSION']
AnoC = ['2011: Local: Vitimas.\n\n Obrigado pela consulta.\n\n END OF TRASMISSION']
AnoD = ['2012: Local: Vitimas.\n\n Obrigado pela consulta.\n\n END OF TRASMISSION']
AnoE = ['2013: Local: Vitimas.\n\n Obrigado pela consulta.\n\n END OF TRASMISSION']
AnoF = ['2014: Local: Vitimas.\n\n Obrigado pela consulta.\n\n END OF TRASMISSION']
AnoG = ['2015: Local: Vitimas.\n\n Obrigado pela consulta.\n\n END OF TRASMISSION']
AnoH = ['2016: Local: Vitimas.\n\n Obrigado pela consulta.\n\n END OF TRASMISSION']
AnoI = ['2017: Local: Vitimas.\n\n Obrigado pela consulta.\n\n END OF TRASMISSION']

# 2 Configuração do Menu
def menu():
    print("\tMENU\n")
    print("\t1 - Escanear")
    print("\t2 - Sobre")
    print("\t3 - Sair\n")
    selection = int(input("Digite o numero do menu que deseja acessar: "))
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
        print("Escolha incorreta, tente novamente.\n")
        menu()

# 3 Configuração do Scan criada por Adriel Freud
def escanear():
    import time

    raw_input("AGUARDANDO RESPOSTA DO SERVIDOR\n\n\nENTER para confirmar o processo. ")

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
    print ("      `-oooooooooo+-`")
    print ("    .smhh++//+    `/ys.  ")
    print ("  `sMMMNNh/hh/    -:odms` ")
    print (" `hMMMMMmhy/..    +hsshdh`")
    print (" soomMysy-       :mNNhyyms")
    print (" N``-s/o`..`    .MMMMMMMMN")
    print (" N`    .+Nmms.`  :+/oMMMMN")
    print (" so     +NMMMNm-     hMMMs")
    print (" `h/     .NMMmo      +MMd`")
    print ("  `ss.    hNd-       .Ns` ")
    print ("    .os/` :m`     `/so.  ")
    print ("      `-+oosoooooo+-`    \n")

    print ("PROCESSANDO DADOS\n")
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

# 4 Segundo Menu
    selection = int(input("Digite o ano que deseja acessar: "))
    print ("\n")

    if selection == 2009:
        print(AnoA[0])
    elif selection == 2010:
        print(AnoB[0])
    elif selection == 2011:
        print(AnoC[0])
    elif selection == 2012:
        print(AnoD[0])
    elif selection == 2013:
        print(AnoE[0])
    elif selection == 2014:
        print(AnoF[0])
    elif selection == 2015:
        print(AnoG[0])
    elif selection == 2016:
        print(AnoH[0])
    elif selection == 2017:
        print(AnoI[0])

    else:
        print("Escolha incorreta, reinicie o programa.\n")
        menu()

def sobre():
    print("Sobre: Este programa foi desenvolvido em python.\n")

print menu()
